from . import views
from django.urls import path

urlpatterns = [
    #path('', views.HomePage.as_view(), name='home'),
    path('', views.BlogPostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

