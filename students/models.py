from django.db import models
from django.contrib.auth.models import ( User)

# Create your models here.
class MyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course_name = models.CharField(max_length=100,blank=True, null=True)
