from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('create/', views.create, name='create'),
    path('createorder/<str:pk>', views.createorder, name='createorder'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/' , views.userProfile, name='userProfile'),
]
