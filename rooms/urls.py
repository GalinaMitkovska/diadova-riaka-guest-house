from django.urls import path
from rooms import views
urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('add/', views.room_create, name='room_create'),
    path('<int:pk>/edit/', views.room_edit, name='room_edit'),
    path('<int:pk>/delete/', views.room_delete, name='room_delete'),
]