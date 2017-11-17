from django_countries.widgets import CountrySelectWidget
from django_countries import widgets, countries
from django import forms
from .models import Post, Comment
from django.forms import ModelForm, Textarea


class PostForm(forms.ModelForm):
    #image = forms.Field(max_length=Post._meta.get_field('image').max_length)
    class Meta:
        model = Post
        fields = ('title', 'country', 'image', 'content')
        widgets = {'country': CountrySelectWidget(), 'content': Textarea(attrs={'class': 'form-control' })}

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(PostForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'message')

    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )


    
