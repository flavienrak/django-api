from django.urls import path
from . import views

urlpatterns = [
  path('get-users/', views.getUsers, name='getUsers'),
  path('sign-up', views.signUp, name='sign-up')
]