from django.contrib import admin
from .models import Genre, Movie, Score

class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'audience', 'postser_url', 'description', 'genre_id')

admin.site.registesr(Movie, MovieAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'score', 'movie_id')

admin.site.register(Score, ScoreAdmin)