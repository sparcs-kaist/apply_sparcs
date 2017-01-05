from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sso_uid = models.CharField(max_length=30, primary_key=True)
    #application_set

