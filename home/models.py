from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserRegisted(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True, null=True)
    
  
  