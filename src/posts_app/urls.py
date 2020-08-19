from django.urls import path
from . import views

app_name='posts_app'

urlpatterns = [
    path('post-create/', views.create_post, name='post-create'),
    path('post-update/<int:id>', views.update_post, name='post-update'),
    path('post-details/<int:id>', views.post_details, name='post-details'),
    path('post-list/', views.post_list, name='post-list'),
]
