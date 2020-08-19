from django.urls import path
from . import views

app_name='posts_api'

urlpatterns = [
     path('post-list/', views.PostListAPIVIew.as_view(), name='post-list'),
     path('post-details/<int:pk>', views.PostRetriveAPIView.as_view(), name='post-details'),
     path('post-update/<int:pk>', views.PostUpdateAPIView.as_view(), name='post-update'),
     path('post-delete/<int:pk>', views.PostDeleteAPIView.as_view(), name='post-delete'),
     path('post-create/', views.PostCreateSerializer.as_view(), name='post-create'),
]
