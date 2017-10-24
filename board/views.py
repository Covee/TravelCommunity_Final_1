from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Post


class PostList(View):
    #post = Post.objects.all()
    #context_object_name = 'posts'
    paginate_by = 15


class PostDetail(DetailView):
    model = Post
    template_name = 'korea/post_detail.html'

    '''def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['id'] = Post.objects.filter(pk=self.kwargs.get('pk'))
        return context'''


class KoreaBoard(ListView):
    template_name = 'korea/board.html'
    model = Post





