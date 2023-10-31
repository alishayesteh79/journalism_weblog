from django.views.generic import ListView, DetailView, CreateView 
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy,reverse


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    fields= ("title","body","author")
    template_name = 'article_new.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete.html'
    