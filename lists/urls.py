from django.urls import path
from lists import views

urlpatterns = [
    path('lists/', views.lists_list),
    path('lists/<int:pk>/', views.lists_detail),
]