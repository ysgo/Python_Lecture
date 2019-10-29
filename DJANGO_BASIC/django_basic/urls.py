from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('utilities/', include('utilities.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
