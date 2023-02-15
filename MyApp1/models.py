from django.db import models
from django.core.validators import MinLengthValidator

class product (models.Model):
    event_place = models.CharField (max_length=250, default='place')
    name = models.CharField (max_length = 250, default='place')
    sum = models.CharField (max_length = 250, default='place')
    price = models.CharField (max_length = 250, default='place')
    descp = models.TextField('полное_описание' , blank = True)
    image = models.ImageField(upload_to='static\media\img',  blank = True)
    def __str__ (self):
       
       return self.name + " " + self.price;

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

class cust (models.Model) :   
    name = models.CharField (max_length = 250)
    surname= models.CharField (max_length=250)
    email = models.EmailField(blank=True)
    password = models.CharField (max_length = 250, validators=[MinLengthValidator(8)])
    
    def __str__ (self):
       
       return self.name + " " + self.surname;

    class Meta:
       verbose_name = 'клиент'
       verbose_name_plural = 'клиенты'
# Create your models here.
