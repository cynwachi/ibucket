from django.db import models
#Reads and writes data 
# Create your models here.

class MyWishName(models.Model):
   # """ Atypical class defiing a model, derived from the MOdel class."""
    
    #Fields
    input_your_wish = models.CharField(max_length=30, help_text='Enter your wish')
    #
    
    #METADATA
    class Meta
        ordering =['-input_your_wish']
    
    #Methods
    
    def get_absolute_url(self):
        # """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        #"""String for representing the MyWishName object (in Admin site etc."""
        return self.input_your_wish
