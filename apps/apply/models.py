from django.db import models
from apps.session.models import Circles
# Create your models here.

class Application(models.Model):
    SEMESTER_IN_APPLY = (
        ('SP', 'Spring'),
        ('SU', 'Summer'),
        ('FA', 'Fall'),
        ('WI', 'Winter'),
    )
    user = models.ForeignKey('session.UserProfile', on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.CharField(max_length=2, choices=SEMESTER_IN_APPLY)
    circle_uid = models.ForeignKey(Circles)
    #item_set

class Item(models.Model):
    application = models.ForeignKey('Application', on_delete=models.CASCADE)
    article_name = models.CharField(max_length=256)
    content = models.TextField()




