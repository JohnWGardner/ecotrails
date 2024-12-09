from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('<slug:slug>/edit_recommendation/<int:recommendation_id>', views.recommendation_edit, name='recommendation_edit'),
    path('<slug:slug>/delete_recommendation/<int:recommendation_id>', views.recommendation_delete, name='recommendation_delete'),
]