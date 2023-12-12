from django import forms

from main.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['home_page', 'captcha', 'text', 'parent_comment']
        widgets = {
            'username': forms.HiddenInput(),
            'email': forms.HiddenInput(),
            'parent_comment': forms.HiddenInput(),
        }

