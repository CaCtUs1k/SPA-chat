from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from main.forms import CommentForm
from main.models import Comment
from main.queues import CommentQueue

comment_queue = CommentQueue()


def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid() and request.recaptcha_is_valid:
            comment_queue.add_comment((form, request))

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
