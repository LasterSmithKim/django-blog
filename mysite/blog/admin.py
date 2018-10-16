from django.contrib import admin

# Register your models here.
from . import models

class Article(admin.ModelAdmin):
    list_display = ('title','content','pub_date','update_time')

admin.site.register(models.Article,Article)
