# this is created by gaurav for blog application

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='/'),
    path('article_list/', views.article_list_page, name='article_list_page'),
    path('article/<str:slug>/', views.article_detail_page, name='article'),
    path('whoami/', views.whoami_page, name='whoami_page'),
    path('contactme/', views.contactme_page, name='contactme_page'),
    path('article_create/', views.article_create_page, name='article_create_page')
]

urlpatterns += staticfiles_urlpatterns()
