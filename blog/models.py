from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Gallery(models.Model):
    title = models.CharField(max_length=200)

class ImageVideo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='images/')  

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
