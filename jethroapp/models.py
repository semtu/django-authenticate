from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class form_model(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    email=models.EmailField()
    message=models.TextField()

class user_model(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)

    portfolio=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
