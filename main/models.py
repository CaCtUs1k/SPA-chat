from django.db import models

from main.utils import validate_file_field
from user.models import User


class Comment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    home_page = models.URLField(blank=True, null=True)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    attachment = models.FileField(upload_to='comment_attachments/', null=True, blank=True, max_length=255,
                                  validators=[validate_file_field])

    def __str__(self):
        return f'{self.sender.username} {self.created_at}'

    def get_child_comments(self):
        return Comment.objects.filter(parent_comment=self)
