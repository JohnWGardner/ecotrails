from . import views
from django.urls import path

urlpatterns = [
    #path('', views.HomePage.as_view(), name='home'),
    path('blog/', views.BlogPostList.as_view(), name='home'),
]

