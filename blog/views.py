# this file is created by gaurav

from django.http import Http404, HttpResponse
from django.shortcuts import render,  get_object_or_404
from .models import Article, ContactMeData
from .forms import ContactMeDataForm, ArticleForm


def article_detail_page(request, slug):

    article = get_object_or_404(Article, slug=slug)

    template_name = 'article_detail.html'

    article_list = Article.objects.all()

    context = {'title': 'Gizmo','article': article, 'home': 'active',
               'article_list': article_list}

    return render(request, template_name, context)


def home_page(request):

    template_name = 'home.html'

    article_list = Article.objects.all().order_by(
        '-date_published')[0:6]  # [:-5:-1]

    context = {'title': 'Gizmo - Home',
               'home': 'active', 'article_list': article_list}

    return render(request, template_name, context)


def article_list_page(request):

    template_name = 'article_list.html'

    article_list = Article.objects.all()[::-1]

    context = {'title': 'Gizmo - Articles',
               'articles': 'active', 'article_list': article_list, }

    return render(request, template_name, context)


def whoami_page(request):

    template_name = 'whoami.html'

    context = {'title': 'Gizmo - WhoAmI', 'whoami': 'active'}

    return render(request, template_name, context)


def contactme_page(request):

    form = ContactMeDataForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = ContactMeDataForm()

    template_name = 'contactme.html'

    context = {'title': 'Gizmo - ContactMe',
               'contactme': 'active', 'form': form}

    return render(request, template_name, context)


def article_create_page(request):

    form = ArticleForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Article.writer = request.user
            form = ArticleForm()
    else:
        form = ArticleForm()

    template_name = 'article_create.html'

    context = {'title': 'Gizmo - Create Article',
               'articles': 'active', 'form': form}

    return render(request, template_name, context)
