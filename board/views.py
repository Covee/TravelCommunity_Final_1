from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm


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
    #post = get_object_or_404(Post, pk=pk)
    template_name = 'korea/post_detail.html'
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('korea/post_detail/', pk=pk)
    else:
        form = CommentForm()
    return render(request, '/post_detail.html', {'form': form})


class PostAdd(CreateView):
    model = Post
    template_name = 'korea/post_add.html'
    fields = ['title', 'country','content','image']
    success_url = reverse_lazy('korea')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostAdd, self).form_valid(form)


class PostChange(ListView):
    template_name = 'board/korea/change_list.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'country','content','image']
    success_url = reverse_lazy('board:korea')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('board:korea')


