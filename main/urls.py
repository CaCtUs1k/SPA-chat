from django.urls import path

from main.views import add_comment, ViewComments

app_name = "main"

urlpatterns = [
    path('', ViewComments.as_view(), name='view_comments'),
    path('add_comment/', add_comment, name='add_comment'),
]
