
from django.contrib import admin
from django.urls import path
from storeapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home-alt'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
]

