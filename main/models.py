from django.db import models


class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    home_page = models.URLField(blank=True, null=True)
    captcha = models.CharField(max_length=255)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

    def get_child_comments(self):
        return Comment.objects.filter(parent_comment=self)
