from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, View, TemplateView



class PostList(View):
    posts = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 15
    

    def index(request):
        return render(request, 'korea/post_detail.html')


class korea_board(TemplateView):
    template_name = 'korea/board.html'


#class PostDetail():



