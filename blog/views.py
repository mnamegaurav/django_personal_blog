# this file is created by gaurav

from django.http import Http404, HttpResponse
from django.shortcuts import render,  get_object_or_404
from .models import Article, ContactMeData
from .forms import ContactMeDataForm
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def article_detail_page(request, slug):

    article = get_object_or_404(Article, slug=slug)

    template_name = 'article_detail.html'

    article_list = Article.objects.all()

    context = {'title': 'The Linux Blog','article': article, 'home': 'active',
               'article_list': article_list}

    return render(request, template_name, context)


def home_page(request):

    template_name = 'home.html'

    article_list = Article.objects.all().order_by(
        '-date_published')[0:6]  # [:-5:-1]

    context = {'title': 'The Linux Blog - Home',
               'home': 'active', 'article_list': article_list}

    return render(request, template_name, context)

class ArticleListView(ListView):
    model = Article
    template_name='blog/article_list.html'
    ordering = ['-date_published']

def whoami_page(request):

    template_name = 'whoami.html'

    context = {'title': 'The Linux Blog - WhoAmI', 'whoami': 'active'}

    return render(request, template_name, context)


def contactme_page(request):

    form = ContactMeDataForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = ContactMeDataForm()

    template_name = 'contactme.html'

    context = {'title': 'The Linux Blog - ContactMe',
               'contactme': 'active', 'form': form}

    return render(request, template_name, context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name='blog/article_form.html'
    fields = ['title','slug','description','body']
    success_url="/article_list"

    def form_valid(self,form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    template_name='blog/article_form.html'
    fields = ['title','slug','description','body']
    success_url="/article_list"

    def form_valid(self,form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.writer:
            return True
        return False 


class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    success_url="/article_list"

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.writer:
            return True
        return False 