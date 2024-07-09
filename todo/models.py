from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    review_name = models.CharField(max_length=50)
    review_title = models.CharField(max_length=50)
    task=models.ForeignKey(Task,on_delete=models.CASCADE)