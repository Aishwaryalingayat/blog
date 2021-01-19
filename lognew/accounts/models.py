from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic')
    

class Acc(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def likes(self):
        post_likes=PostLike.objects.filter(post_id=self.id).count()
        return post_likes    

class PostLike(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post =models.ForeignKey(Acc, on_delete=models.CASCADE)

    