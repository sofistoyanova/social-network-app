from rest_framework.serializers import ModelSerializer, SerializerMethodField

from ..models import Comment

class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()

    def get_user(self, obj):
        return str(obj.user.username)

    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'content', 'created', 'user']
        #fields = ['id', 'content_type', 'object_id', 'content', 'created', 'user']
