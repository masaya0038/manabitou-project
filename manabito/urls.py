from django.urls import path, include
from manabito import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.manabitohome, name='manabitohome'),
]
