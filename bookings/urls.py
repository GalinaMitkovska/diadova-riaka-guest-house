from django.urls import path
from bookings import views
urlpatterns = [
path('', views.booking_list, name='booking_list'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('add/', views.booking_create, name='booking_create'),
    path('<int:pk>/edit/', views.booking_edit, name='booking_edit'),
    path('<int:pk>/delete/', views.booking_delete, name='booking_delete'),
]