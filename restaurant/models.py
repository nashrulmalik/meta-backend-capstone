from django.db import models


class Menu(models.Model):
   name  = models.CharField(max_length=100) 
   price = models.IntegerField() 
   description = models.TextField(max_length=1000,default='')

   def __str__(self):
      return f'{self.name} : {str(self.price)}'


class Booking(models.Model):
   tableno = models.IntegerField()
   persons = models.IntegerField()

