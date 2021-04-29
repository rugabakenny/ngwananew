from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserRegisted(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True, null=True)


    
class Hotel(models.Model):
    image = models.ImageField(max_length=255)
    location = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
   
  
    
    def _str_(self):
        return self.title 
    
class Travel(models.Model):
    image = models.ImageField(max_length=255)
    location = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
   
  
    
    def _str_(self):
        return self.title 
class Currency(models.Model):
    image = models.ImageField(max_length=255)
    location = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
   
  
    
    def _str_(self):
        return self.title 



class Mokoro(models.Model):
    image = models.ImageField(max_length=255)
    location = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
   
  
    
    def _str_(self):
        return self.title 
  

class Boat(models.Model):
    image = models.ImageField(max_length=255)
    location = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
   
  
    
    def _str_(self):
        return self.title 
  