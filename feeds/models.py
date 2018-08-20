from django.db import models

from accounts.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    datetime_created = models.DateTimeField(auto_now_add=True)