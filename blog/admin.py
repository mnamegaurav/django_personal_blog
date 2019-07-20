from django.contrib import admin

# Register your models here.
from .models import Article, UserData

#registration for Article model
admin.site.register(Article)

#registration for UserData model
admin.site.register(UserData)
