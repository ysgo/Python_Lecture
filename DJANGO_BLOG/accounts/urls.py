from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('quit/', views.quit, name='quit'),
    path('edit/', views.edit, name='edit'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/profile/', views.profile, name='profile'),
]