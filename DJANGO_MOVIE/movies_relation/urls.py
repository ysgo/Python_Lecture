from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
