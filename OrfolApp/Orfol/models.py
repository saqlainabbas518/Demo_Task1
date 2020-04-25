from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import math
from django.urls import reverse


class Category(models.Model):
    CATEGORIES = (('Accessories', 'Accessories'),
                  ('Books', 'Books'),
                  ('clothing', 'Female'),
                  ('computing', 'computing'),
                  ('Documents', 'Documents'),
                  ('humans', 'humans'),
                  ('Keys', 'Keys'),
                  ('machinary', 'machinary'),
                  ('money', 'money'),
                  ('mobile', 'mobile'),
                  ('sports', 'sports'),)
    categories = models.CharField(max_length=50,choices=CATEGORIES,default="E")
    icon = models.ImageField(default='default.jpg', upload_to='Categories_pics')

    def __str__(self):
        return f'{self.categories}'



class Subcategory(models.Model):
    SUBCATEGORIES = (('Found', 'Found'),
                     ('Lost', 'Lost'),)
    subcategories = models.CharField(max_length=50,choices=SUBCATEGORIES,default="Lost")

    def __str__(self):
        return f'{self.subcategories}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default='default.jpg' , upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



class Report(models.Model):
    title =models.CharField(max_length=150)
    categories = models.ForeignKey(Category , on_delete=models.CASCADE ,default='Accessories')
    subcategories=models.ForeignKey(Subcategory , on_delete=models.CASCADE , default='Lost')
    city = models.CharField(max_length=50)
    subcity = models.CharField(max_length=80)
    image = models.ImageField(default='default.jpg',upload_to='report_pics')
    reward = models.IntegerField(null=True, blank=True )
    description = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} Report'

    def get_absolute_url(self):
        return reverse('report')

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.time

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds / 60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds / 3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days / 30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days / 365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"
















