from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('login/', views.loginPage, name='loginPage'),
    path('sign-up/', views.signUpPage, name='signUpPage'),
    path('chat/', views.chat, name='chat'),
]