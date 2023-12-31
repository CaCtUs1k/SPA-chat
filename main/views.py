import bleach
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from main.forms import CommentForm
from main.models import Comment
from main.utils import compress_image


@login_required
def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid() and request.recaptcha_is_valid:
            parent_comment_id = request.POST.get("parent_id")
            parent_comment = None
            if parent_comment_id:
                parent_comment = Comment.objects.get(pk=parent_comment_id)

            allowed_tags = ["i", "strong", "a", "code"]
            cleaned_text = bleach.clean(
                form.cleaned_data.get("text"), tags=allowed_tags
            )
            file = form.cleaned_data.get("file")

            if file:
                compress_image(file)

            Comment.objects.create(
                home_page=form.cleaned_data.get("home_page"),
                text=cleaned_text,
                parent_comment=parent_comment,
                sender=request.user,
                attachment=file,
            )

    return redirect("/")


class ViewComments(LoginRequiredMixin, ListView):
    model = Comment
    template_name = "comments/view_comments.html"
    context_object_name = "comments"
    login_url = "accounts/login/"
    paginate_by = 25

    def get_queryset(self):
        queryset = Comment.objects.select_related(
            "parent_comment", "sender"
        ).filter(parent_comment=None)
        ordering = self.get_ordering()
        queryset = queryset.order_by(ordering)

        if self.request.GET.get("reverse"):
            queryset = queryset.reverse()

        return queryset

    def get_ordering(self):
        ordering = self.request.GET.get("ordering", "created_at")

        if ordering in ["username", "email"]:
            return f"sender__{ordering}"

        return "created_at"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["ordering"] = self.get_ordering()
        context["form"] = CommentForm()
        context["reverse"] = self.request.GET.get("reverse")

        return context

    def post(self, request, *args, **kwargs):
        add_comment(request)
