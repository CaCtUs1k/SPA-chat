import bleach
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from main.forms import CommentForm
from main.models import Comment


@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            if request.recaptcha_is_valid:
                parent_comment_id = form.cleaned_data.get('parent_comment')
                parent_comment = None
                if parent_comment_id:
                    parent_comment = Comment.objects.get(pk=parent_comment_id)

                allowed_tags = ['i', 'strong', 'a', 'code']
                cleaned_text = bleach.clean(form.cleaned_data.get('text'), tags=allowed_tags)
                Comment.objects.create(
                    home_page=form.cleaned_data.get('home_page'),
                    text=cleaned_text,
                    parent_comment=parent_comment,
                    username=request.user.username,
                    email=request.user.email,
                    attachment=form.cleaned_data.get('file')
                )
                return redirect('main:view_comments')
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment.html', {'form': form})


class ViewComments(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'comments/view_comments.html'
    context_object_name = 'comments'
    login_url = 'accounts/login/'
    paginate_by = 25

    def get_queryset(self):
        queryset = Comment.objects.filter(parent_comment=None)
        ordering = self.get_ordering()
        queryset = queryset.order_by(ordering)
        if self.request.GET.get('reverse'):
            queryset = queryset.reverse()
        return queryset

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'created_at')
        if ordering in ['username', 'email', 'created_at']:
            return ordering
        return 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordering'] = self.get_ordering()
        context['reverse'] = self.request.GET.get('reverse')
        return context
