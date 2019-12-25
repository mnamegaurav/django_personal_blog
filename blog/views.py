 # this file is created by gaurav

from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import render,  get_object_or_404,redirect
from .models import Article, ContactMeData, Comment
from .forms import ContactMeDataForm, CommentForm
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

    template_name = 'blog/article_detail.html'

    article_list = Article.objects.all()
    
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        liked = True


    comments = Comment.objects.filter(article=article).order_by('-date_time')
    comment_form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(article=article,user=request.user,content=content)
            comment.save()
            return HttpResponseRedirect(article.get_absolute_url())

    context = {'title': 'The Linux Blog','article': article, 'home': 'active',
               'article_list': article_list,'liked':liked,'comments':comments,'comment_form':comment_form}

    return render(request, template_name, context)

def article_likes_dislikes(request):
    article = get_object_or_404(Article,id=request.POST.get('article_id'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        article.dislikes.add(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        article.dislikes.remove(request.user)
        liked = True
    return HttpResponseRedirect(article.get_absolute_url())


def home_page(request):

    template_name = 'blog/home.html'

    article_list = Article.objects.all().order_by('-date_published')[0:6]

    context = {'title': 'The Linux Blog - Home',
               'home': 'active', 'article_list': article_list}

    return render(request, template_name, context)


def whoami_page(request):

    template_name = 'blog/whoami.html'

    context = {'title': 'The Linux Blog - WhoAmI', 'whoami': 'active'}

    return render(request, template_name, context)


def contactme_page(request):

    form = ContactMeDataForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = ContactMeDataForm()

    template_name = 'blog/contactme.html'

    context = {'title': 'The Linux Blog - ContactMe',
               'contactme': 'active', 'form': form}

    return render(request, template_name, context)


class ArticleListView(ListView):
    model = Article
    template_name='blog/article_list.html'
    ordering = ['-date_published']

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name='blog/article_form.html'
    fields = ['title','slug','description','body','category']
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