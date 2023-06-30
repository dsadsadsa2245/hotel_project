from django.urls import path, include
from rest_framework.routers import DefaultRouter
from autorization import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('', views.UserListView.as_view()),
    path('login/',views.UserLoginView.as_view()),
]
