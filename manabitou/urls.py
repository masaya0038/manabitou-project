
from django.contrib import admin
from django.urls import path, include
from manabiron import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('manabito/',include('manabito.urls')),
    path('manabiron/',include('manabiron.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
