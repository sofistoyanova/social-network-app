from django.db import models
from django.contrib.auth.models import User

class UserVisits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    ip_address = models.CharField(max_length=250)
    session_key = models.CharField(max_length=250)
