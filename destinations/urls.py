from . import views
from django.urls import path

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('edit_recommendation/<int:recommendation_id>', views.recommendation_edit, name='recommendation_edit'),
    path('delete_recommendation/<int:recommendation_id>', views.recommendation_delete, name='recommendation_delete'),
]
