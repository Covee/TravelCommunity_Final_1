from django_countries.widgets import CountrySelectWidget
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'country')
        widgets = {'country': CountrySelectWidget()}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('user', 'message')

	comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )

    
