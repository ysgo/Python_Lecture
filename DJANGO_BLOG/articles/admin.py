from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'create_at', 'update_at')    

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'create_at', 'article_id')

admin.site.register(Comment, CommentAdmin)
