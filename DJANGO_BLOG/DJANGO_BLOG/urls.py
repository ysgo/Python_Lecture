from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('students/', include('students.urls')),
    path('doppelganger/', include('doppelganger.urls')),
]
