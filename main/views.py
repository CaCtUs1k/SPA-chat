from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from main.forms import CommentForm
from main.models import Comment


@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if not request.recaptcha_is_valid:
                messages.error(request, "Invalid reCAPTCHA. Please try again.")
            else:
                parent_comment_id = form.cleaned_data.get('parent_comment')
                parent_comment = None
                if parent_comment_id:
                    parent_comment = Comment.objects.get(pk=parent_comment_id)
                Comment.objects.create(
                    home_page=form.cleaned_data.get('home_page'),
                    text=form.cleaned_data.get('text'),
                    parent_comment=parent_comment,
                    username=request.user.username,
                    email=request.user.email
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
        return Comment.objects.filter(parent_comment=None)
