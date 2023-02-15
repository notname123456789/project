from django.db import models
from django.core.validators import MinLengthValidator

#what_trash = [('свалка' , 'свалка') , ('помойка' , 'помой-ка') , ('тот случай когда мусор это ты' , 'тот случай когда мусор это ты')]

class news (models.Model):
    name = models.CharField (max_length = 250 )
    descp = models.TextField('полное_описание' , blank = True)
    image = models.ImageField(upload_to='static\media\img',  blank = True)

    #kind_of = models.CharField (max_length = 250 , choices = what_trash)
    def __str__ (self):      
       return self.name;

    class Meta:
        verbose_name = 'новости'
        verbose_name_plural = 'новости'

class some_new (models.Model):
     name = models.CharField (max_length = 250 )
     descp = models.TextField('полное_описание' , blank = True)
     image = models.ImageField(upload_to='static\media\img',  blank = True)

     #kind_of = models.CharField (max_length = 250 , choices = what_trash)
     def __str__ (self):      
        return self.name;

     class Meta:
         verbose_name = 'предложение извне'
         verbose_name_plural = 'предложение извне'
#///////////////////////////////////////////////////////////////////////////////////////

class some_new_fs (models.Model):
     name = models.CharField (max_length = 250 )
     descp = models.TextField('полное_описание' , blank = True)
     image = models.ImageField(upload_to='static\media\img',  blank = True)
     student_name = models.CharField (max_length = 250 )
     #kind_of = models.CharField (max_length = 250 , choices = what_trash)
     def __str__ (self):      
        return self.name;

     class Meta:
         verbose_name = 'предложение от учиника(цы)'
         verbose_name_plural = 'предложение от учиника(цы)'

#///////////////////////////////////////////////////////////////////////////////////////

class student (models.Model):
    name = models.CharField (max_length = 250)
    password = models.CharField (max_length = 250, validators=[MinLengthValidator(8)])
    def __str__ (self):
       
      return self.name;

    class Meta:
       verbose_name = 'ученик'
       verbose_name_plural = 'ученики'

class rast (models.Model):
    name = models.CharField (max_length = 250)
    surname = models.CharField (max_length = 250)
    desс = models.TextField('информация об учинике: ' , blank = True)
    rt = models.CharField ('место в рейтинге: ' , max_length = 250)
    image = models.ImageField(upload_to='static\media\img',  blank = True)
    def __str__ (self):
       
      return self.name;

    class Meta:
       verbose_name = '_ученик_'
       verbose_name_plural = '_ученики_'

# Create your models here.
