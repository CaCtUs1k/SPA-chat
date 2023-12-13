from django import forms


class CommentForm(forms.Form):
    home_page = forms.URLField(required=False)
    text = forms.CharField(widget=forms.Textarea)
    parent_comment = forms.IntegerField(required=False, widget=forms.HiddenInput())

