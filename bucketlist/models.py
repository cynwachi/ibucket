from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db.models.fields import DateTimeField, TextField, CharField

# Create your models here.
CHOICES = [("play", "Play"), ("pray", "Pray")]

class User(AbstractUser):
    pass

class PrayPlay(models.Model):
    text = models.TextField(max_length=150,)
    date_time = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name="play_prays")
    type = models.CharField(choices=CHOICES, max_length=150)
    
    def __str__(self):
        #"""String for representing the MyWishName object (in Admin site etc. used any place you "RENDER"    """
        return self.text