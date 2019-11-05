from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('students/', include('students.urls')),
    path('doppelganger/', include('doppelganger.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
