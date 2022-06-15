from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Cover(models.Model):
    url = models.CharField(max_length=100)
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='cover')
