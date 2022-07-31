import uuid
from django.db import models

# Create your models here.
class Config(models.Model):
    urlIdCsd = models.CharField(max_length=500, null=False, unique=False, default='')
    urlRowCsd = models.CharField(max_length=500, null=False, unique=False, default='')
    logoGeoApp = models.ImageField(upload_to='GeoApp', unique=False, default='')
    version = models.CharField(max_length=25, null=False, unique=False, default='')
    
    def __str__(self):
        return '%s: %s' % (self.urlIdCsd, self.urlRowCsd)