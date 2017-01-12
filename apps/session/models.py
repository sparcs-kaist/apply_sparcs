from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Circles(models.Model):
    circle_name = models.CharField(max_length=255, default='', primary_key=True)
    circle_uid = models.IntegerField(blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sso_uid = models.CharField(max_length=30, primary_key=True)
    circle_staff = models.ManyToManyField(Circles)
    # application_set


