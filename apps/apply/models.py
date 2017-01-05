from django.db import models
# Create your models here.

class Application(models.Model):
    SEMESTER_IN_APPLY = (
        ('SP', 'Spring'),
        ('SU', 'Summer'),
        ('FA', 'Fall'),
        ('WI', 'Winter'),
    )
    user_id = models.ForeignKey('session.UserProfile', on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.CharField(max_length=2, choices=SEMESTER_IN_APPLY)
    #item_set

class Item(models.Model):
    application_id = models.ForeignKey('Application', on_delete=models.CASCADE)
    article_name = models.CharField(max_length=256)
    content = models.TextField()




