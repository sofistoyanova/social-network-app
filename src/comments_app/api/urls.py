from django.urls import path
from . import views

app_name='comments_api'

urlpatterns = [
     path('comment-list/', views.CommentListAPIVIew.as_view(), name='comment-list'),
     path('comment-delete/<int:pk>', views.CommentDeleteAPIView.as_view(), name='comment-delete'),
     path('comment-create/', views.CommentCreateSerializer.as_view(), name='comment-create'),
]
