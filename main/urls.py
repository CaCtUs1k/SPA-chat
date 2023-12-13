from django.urls import path

from main.decorators import check_recaptcha
from main.views import add_comment, ViewComments

app_name = "main"

urlpatterns = [
    path('', ViewComments.as_view(), name='view_comments'),
    path('add_comment/', check_recaptcha(add_comment), name='add_comment'),
]
