from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db.models.fields import DateTimeField, TextField, CharField
from localflavor.us.models import USStateField, USZipCodeField

#from metadata.mixins import MetadataMixin
#Reads and writes data 
# Create your models here.
CHOICES = [("play", "Play"), ("pray", "Pray")]

class User(AbstractUser):
    pass

class PrayPlay(models.Model):
    text = models.TextField(max_length=150,)
    date_time = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name="users")
    type = models.CharField(choices=CHOICES)

    #METADATA
    #class Meta(MetadataMixin, models
        #username = models.CharField(max_length=150)
    #Methods
    
    #def get_absolute_url(self):
        # """Returns the url to access a particular instance."""
    #    return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        #"""String for representing the MyWishName object (in Admin site etc. used any place you "RENDER"    """
        return self.text