from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxLengthValidator
import math

class Profile(models.Model):
    user_id  = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    dob = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=80)
    country= models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=80)
    profile_picture = models.ImageField(default='default.jpg', null=True , blank=True , upload_to='profile_picss' )

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=80)
    icon = models.ImageField(upload_to='category_icons')

    def __str__(self):
        return self.name

class SubCategory(models.Model):
      category_id = models.ForeignKey(Category , on_delete=models.CASCADE)
      name = models.CharField(max_length=50)

      def __str__(self):
          return self.name

class Notification(models.Model):
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.CharField(max_length=80)
    action = models.CharField(max_length=80)

    def __str__(self):
        return self.text


CHOICES = [('L','Lost'),('F','Found')]
class Report(models.Model):
    user_id  = models.ForeignKey(User , on_delete=models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(SubCategory , on_delete=models.CASCADE)
    type = models.CharField(max_length=80,choices=CHOICES , default='L')
    title = models.CharField(max_length=80)
    reward = models.CharField(max_length=50)
    location = models.CharField(max_length=80)
    date_occurrence = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)
    description = models.TextField(validators=[MaxLengthValidator(300)])
    class Meta:
        ordering = ['-date_created']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('reportdetail', kwargs= {'pk':self.pk})
    def __unicode__(self):
        return self.user_id

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.date_created

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


class ReportImage(models.Model):
    report_id = models.OneToOneField(Report , on_delete=models.CASCADE)
    imagepath = models.ImageField(default='default.jpg',  null=True , blank=True , upload_to='report_images')

    def __str__(self):
        return str(self.report_id)


class SavedReport(models.Model):
    report_id = models.ForeignKey(Report, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.report_id

