from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Photo(models.Model):
    title = models.CharField(max_length=100, default='Untitled')  # Add a default value
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title