
from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    

    def __str__(self):
        return '{} {}'.format(self.name,self.category)
    
    category=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.CharField(max_length=100)
    image =models.ImageField(blank=True,upload_to='images')
    stock=models.IntegerField()
    size=models.IntegerField()
    date=models.DateField(auto_now_add=True)

    