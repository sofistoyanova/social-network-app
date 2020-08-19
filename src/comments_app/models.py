from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):
    def get_post_comments(self, post):
        content_type = ContentType.objects.get_for_model(post.__class__)
        object_id = post.id
        comments = Comment.objects.filter(post_id=object_id)
        return comments


class Comment(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    post_id = models.ForeignKey('posts_app.Post', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = CommentManager()

    def __str__(self):
        return self.user.username
