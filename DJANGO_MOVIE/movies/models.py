from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)
    title_en = models.CharField(max_length=70)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()