from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogPostList.as_view(), name='blog'),  # Maps the root URL to the BlogPostList view
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Maps a URL with a slug to the post_detail view
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),  # Maps a URL with a slug and a comment ID to the comment_edit view
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]

