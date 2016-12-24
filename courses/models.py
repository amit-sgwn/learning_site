from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=250)
    description = models.TextField()