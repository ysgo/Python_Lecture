from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번 글 = {self.title} : {self.content}'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Article({self.article_id}) : Comment({self.id})> - {self.content}'