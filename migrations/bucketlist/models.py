from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db.models.fields import DateTimeField, TextField
from localflavor.us.models import USStateField, USZipCodeField

#from metadata.mixins import MetadataMixin
#Reads and writes data 
# Create your models here.

class User(models.Model):
   phone_regex=RegexValidator(
       regex=r'^\+?\d{10$',
       message="Phone number must be entered in the format: '+9999999999'.")
   
   name =models.CharField(max_length=255)
   email = models.EmailField(null=True, blank=True)
   phone_number = models.CharField(max_length=11,
                                   validators=[phone_regex],
                                   null=True,
                                   blank=True)
   address_1 = models.CharField(max_length=255, null=True, blank=True)
   address_2 = models.CharField(max_length=255, null=True, blank=True)
   city = models.CharField(max_length=255, null=True, blank=True)
   state = USStateField(null=true,blank=True)
   zip_code = USZipCodeField(null=true,blank=True)
   birthday = models.CharField(null=True, blank=True)
   
   def __str__(self):
       return self.name

class Play(models.Model):
    text = models.TextField(max_length=150,)
    date_time = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name="users")

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
    
class Pray(models.Model):
        text = models.TextField(max_length=150)
    
    #def get_absolute_url(self):
        # """Returns the url to access a particular instance of Pray."""
    #    return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        #"""String for representing the Pray object (in Admin site etc."""
        return self.text
