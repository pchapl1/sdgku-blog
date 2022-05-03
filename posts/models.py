from django.db import models
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=245)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args = [self.id])