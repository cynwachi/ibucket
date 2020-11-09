from django.db import models

#from metadata.mixins import MetadataMixin
#Reads and writes data 
# Create your models here.

class MyPrayerName(models.Model):
   input_your_prayer = models.CharField(max_length=30, help_text='Enter your wish')
    
    
    #METADATA
    #class Meta(MetadataMixin, models
        #username = models.CharField(max_length=150)
    #Methods
    
    def get_absolute_url(self):
        # """Returns the url to access a particular instance of MyPrayerName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        #"""String for representing the MyWishName object (in Admin site etc."""
        return self.input_your_wish
