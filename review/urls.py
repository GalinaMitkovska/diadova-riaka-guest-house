from django.urls import path
from review import views
urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('delete/<int:pk>/', views.review_delete, name='review_delete'),
]
