from django.urls import path, include
from manabiron import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:manabiron_id>',views.detail, name='detail'),
    path('<int:manabiron_id>/upvote',views.upvote, name='upvote'),
    path('', views.manabironhome, name='manabironhome'),
]
