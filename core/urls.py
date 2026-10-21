from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('attractions/', views.attractions_view, name='attractions'),
]