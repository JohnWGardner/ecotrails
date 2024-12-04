from . import views
from django.urls import path

urlpatterns = [
    path('', views.my_destinations, name='destinations'),
]