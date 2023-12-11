from django.urls import path

from main.views import view_comments, add_comment

urlpatterns = [
    path('', view_comments, name='view_comments'),
    path('add_comment/', add_comment, name='add_comment'),
]
