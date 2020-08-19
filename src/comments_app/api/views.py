from rest_framework import generics
from ..models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from rest_framework.filters import SearchFilter


class CommentListAPIVIew(generics.ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self, *args, **kwargs):
        comment_list = Comment.objects.all()
        search_term = self.request.GET.get('search_term')
        if search_term:
            comment_list = comment_list.filter(title__icontains=search_term)

        return comment_list


class CommentCreateSerializer(generics.CreateAPIView):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            serializer.save(user=self.request.user)


class CommentDeleteAPIView(generics.DestroyAPIView):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer
