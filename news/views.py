from django.shortcuts import get_object_or_404, render
from .models import Post
from .filters import  PostFilter
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .forms import NewsForm
from django.urls import reverse_lazy
from django_filters.views import FilterView


class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_not_author'] = not user.groups.filter(name='authors').exists() if user.is_authenticated else False
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'posst'


class NewsSearch(FilterView):
    model = Post
    template_name = 'news/news_search.html'
    filterset_class = PostFilter
    context_object_name = 'searchs'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news/news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NW'  # Устанавливаем как новость
        return super().form_valid(form)


class ArticleCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news/article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AR'  # Устанавливаем как статью
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news/news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')  # Укажи нужный путь
