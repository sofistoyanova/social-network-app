from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField
from ..models import Post
from django.contrib.contenttypes.models import ContentType
from comments_app.api.serializers import CommentSerializer
from comments_app.models import Comment


class PostListSerializer(ModelSerializer):
    user = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name='posts_api:post-details')
    delete_url = HyperlinkedIdentityField(view_name='posts_api:post-delete')
    update_url = HyperlinkedIdentityField(view_name='posts_api:post-update')

    def get_user(self, obj):
        return str(obj.user.username)

    class Meta:
        model = Post
        fields = ['id','title', 'image', 'content', 'created', 'user', 'url', 'delete_url', 'update_url']


class PostDetailsSerializer(ModelSerializer):
    user = SerializerMethodField()
    comments = SerializerMethodField()
    delete_url = HyperlinkedIdentityField(view_name='posts_api:post-delete')
    update_url = HyperlinkedIdentityField(view_name='posts_api:post-update')

    def get_user(self, obj):
        return str(obj.user.username)

    def get_comments(self, obj):
        comments_qs =  Comment.objects.get_post_comments(obj)
        comments = CommentSerializer(comments_qs, many=True).data
        return comments

    class Meta:
        model = Post
        fields = ['id','title', 'image', 'content', 'created', 'delete_url', 'update_url', 'comments','user']


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
