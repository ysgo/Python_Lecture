from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'create_at', 'update_at')    

admin.site.register(Article, ArticleAdmin)
