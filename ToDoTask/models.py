from django.db import models


# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    task_priority = models.CharField(max_length=25)
    task_status = models.CharField(max_length=20, default='Not Completed')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
