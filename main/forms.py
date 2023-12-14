from django import forms

from main.utils import validate_file_field


class CommentForm(forms.Form):
    home_page = forms.URLField(required=False)
    text = forms.CharField(widget=forms.Textarea)
    parent_comment = forms.IntegerField(required=False, widget=forms.HiddenInput())
    file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'enctype': 'multipart/form-data'}),
        validators=[validate_file_field]
    )

