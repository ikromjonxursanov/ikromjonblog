from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model =Article
    fields =('title', 'summary', 'body', 'photo',)
    template_name="article/article_edit.html"

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super(). form_valid(form)

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user


class ArticleConfirmDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Article
    template_name ='article/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model=Article
    fields =('title', 'summary', 'body', 'photo',)
    template_name = 'article/yangi_post.html'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(). form_valid(form)

    # def test_func(self):
    #     return self.request.user.is_superuser

