from django import forms

from main.utils import validate_file_field


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    home_page = forms.URLField(required=False)
    parent_comment = forms.IntegerField(required=False, widget=forms.HiddenInput())
    file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'enctype': 'multipart/form-data'}),
        validators=[validate_file_field]
    )

