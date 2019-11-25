# this is created by gaurav for blog application

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from .views import ArticleListView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView

urlpatterns = [
    path('', views.home_page, name='/'),
    path('article_list/', ArticleListView.as_view(), name='article_list_page'),
    path('article/<str:slug>/', views.article_detail_page, name='article'),
    path('article/<str:slug>/edit', ArticleUpdateView.as_view(), name='article_edit_page'),
    path('article/<str:slug>/delete', ArticleDeleteView.as_view(), name='article_delete_page'),
    path('whoami/', views.whoami_page, name='whoami_page'),
    path('contactme/', views.contactme_page, name='contactme_page'),
    path('article_create/', ArticleCreateView.as_view(), name='article_create_page')
]

urlpatterns += staticfiles_urlpatterns()
