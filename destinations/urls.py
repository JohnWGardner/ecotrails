from django.urls import path
from . import views

urlpatterns = [
    path('', views.DestinationList.as_view(), name='destination_list'),
    path('<slug:slug>/', views.destination_detail, name='destination_detail'),
]