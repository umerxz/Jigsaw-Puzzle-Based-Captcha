from distutils.command.upload import upload
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Images(models.Model):
    img = models.ImageField(null=True,blank=True,max_length=1000001)#upload_to

    def get_id(self):
        return self.id

class Partition(models.Model):
    partition_id=models.ForeignKey(Images, on_delete=models.CASCADE,null=True,blank=True)
    position=models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(1),MaxValueValidator(9)])
    sliced_img=models.ImageField(null=True,blank=True,max_length=100000)#upload_to
    