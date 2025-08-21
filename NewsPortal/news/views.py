from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Author, PostCategory
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy

from datetime import datetime
from django.shortcuts import render

class PostList(ListView):
    model = Post
    user = 'name'

    template_name = 'post.html'

    context_object_name = 'post'
    queryset = Post.objects.order_by('-time_creation')
    paginate_by = 10 # вот так мы можем указать количество записей на странице


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    template_name = 'posts_detail'
    queryset = Post.objects.all()
    success_url = reverse_lazy('post_list')

class PostCreate(CreateView):
    template_name = 'post_edit.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')

class NewsCreateView(PostCreate):
    def form_valid(self, form):
        form.instance.category_type = 'NW'
        return super().form_valid(form)


class ArticleCreateView(PostCreate):
    def form_valid(self, form):
        form.instance.category_type = 'AR'
        return super().form_valid(form)

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

class NewsUpdateView(PostUpdate):
    def form_valid(self, form):
        form.instance.category_type = 'NW'
        return super().form_valid(form)

class ArticleUpdateView(PostUpdate):
    def form_valid(self, form):
        form.instance.category_type = 'AR'
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'news'
    ordering = ['-time_creation']
    success_url = reverse_lazy('post_list')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
