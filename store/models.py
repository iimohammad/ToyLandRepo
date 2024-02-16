from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Gallery(models.Model):
    title = models.CharField(max_length=200)

class ImageVideo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='images/')  

class UserComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    # Add other fields as needed
