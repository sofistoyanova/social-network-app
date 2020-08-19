from rest_framework import generics
from ..models import Post
from .serializers import PostListSerializer, PostDetailsSerializer, PostCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAuthor
from rest_framework.filters import SearchFilter

class PostCreateSerializer(generics.CreateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostCreateSerializer
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            serializer.save(user=self.request.user)


class PostListAPIVIew(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetriveAPIView(generics.RetrieveAPIView):
        queryset = Post.objects.all()
        serializer_class = PostDetailsSerializer


class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostDetailsSerializer
        permission_classes = [IsAuthenticated, IsAuthor]

        def perform_update(self, serializer):
            serializer.save(user=self.request.user)


class PostDeleteAPIView(generics.DestroyAPIView):
        queryset = Post.objects.all()
        serializer_class = PostDetailsSerializer
        permission_classes = [IsAuthenticated, IsAuthor]
