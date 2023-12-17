from django.contrib import admin

from main.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
