
from django.contrib import admin
from django.urls import path, include
from manabiron import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('manabito/',include('manabito.urls'))
]
