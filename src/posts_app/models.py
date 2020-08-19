from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from comments_app.models import Comment

class Post(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def find_post_details(self):
        return reverse('posts_app:post-details', kwargs={'id': self.id})
