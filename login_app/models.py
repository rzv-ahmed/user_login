from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fb_id=models.URLField(blank=True)
    image=models.ImageField(upload_to='profilepics',blank=True)

    def __str__(self) :
        return self.user.username

    
