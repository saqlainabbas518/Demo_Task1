from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    username = models.ForeignKey(User , on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('allposts')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics')



