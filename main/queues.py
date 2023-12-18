import queue
import threading

import bleach

from main.models import Comment
from main.utils import compress_image


class CommentQueue:
    def __init__(self):
        self._queue = queue.Queue()
        threading.Thread(target=self._process_comments, daemon=True).start()

    def add_comment(self, comment_data):
        self._queue.put(comment_data)

    def _process_comments(self):
        while True:
            comment_data = self._queue.get()
            self._process_comment(comment_data)

    def _process_comment(self, comment_data):
        form, request = comment_data
        parent_comment_id = request.POST.get("parent_id")
        parent_comment = None
        if parent_comment_id:
            parent_comment = Comment.objects.get(pk=parent_comment_id)

        allowed_tags = ["i", "strong", "a", "code"]
        cleaned_text = bleach.clean(form.cleaned_data.get("text"), tags=allowed_tags)
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
