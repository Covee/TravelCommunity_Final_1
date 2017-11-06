from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Post, Comment


class PostList(ListView):
	model = Post
    #template_name = 'korea/board.html'
    #paginate_by = 9
    #queryset = Post.objects.all()


class PostDetail(DetailView):
    model = Post
    template_name = 'korea/post_detail.html'


class KoreaBoard(ListView):
    template_name = 'korea/board.html'
    model = Post



def add(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('board.korea.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'board.korea.post_detail', {'form': form})




