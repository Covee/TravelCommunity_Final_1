from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Post


class PostList(View):
	model = Post
    #post = Post.objects.all()
    #context_object_name = 'posts'
    #paginate_by = 15


class PostDetail(DetailView):
    model = Post
    template_name = 'korea/post_detail.html'


class KoreaBoard(ListView):
    template_name = 'korea/board.html'
    model = Post






