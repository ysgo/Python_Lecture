from django.urls import path
from . import views

app_name = 'movies_relation'

urlpatterns = [
    path('', views.index, name='index'),
]
