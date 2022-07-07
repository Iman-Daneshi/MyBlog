from typing import OrderedDict
from venv import create
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False) 
    tags = models.ManyToManyField('tag', blank=True)
    vote_total = models.IntegerField(null=True, blank=True, default=0)
    vote_ratio = models.IntegerField(null=True, blank=True, default=0)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_date',]


class Review(models.Model):
    VOTE_TYPE =(
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    #owner
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=255, choices=VOTE_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    def __str__(self) -> str:
        return self.value
        
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name