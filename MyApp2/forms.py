from django.forms import ModelForm , TextInput , EmailInput , PasswordInput , FileInput
from .models import some_new
from .models import some_new_fs
from .models import student 
#from .models import what_trash
from django import forms
class some_new_f(ModelForm):
    class Meta:
        model = some_new
        fields = ['name','descp','image']

        widgets = {
            "name": TextInput (attrs = { 'placeholder': 'название'}),
            #"kind_of": forms.Select(attrs={'help': 'AAAAAAAAA'} , choices = what_trash  ),
            "inf" : TextInput (attrs = { 'placeholder': 'описание'}),
            "png" : FileInput (attrs = { 'placeholder': 'изображение'})
            }

class st_new_f(ModelForm):
    class Meta:
        model = some_new_fs
        fields = ['name','descp','image']

        widgets = {
            "name": TextInput (attrs = { 'placeholder': 'название'}),
            #"kind_of": forms.Select(attrs={'help': 'AAAAAAAAA'} , choices = what_trash  ),
            "inf" : TextInput (attrs = { 'placeholder': 'описание'}),
            "png" : FileInput (attrs = { 'placeholder': 'изображение'})
            }

class st_form (ModelForm):
    class Meta:
        model = student
        fields = ['name','password']
        widgets = {
            "name": TextInput (attrs = { 'placeholder': 'имя'}),
            "password": TextInput (attrs = { 'placeholder': 'пароль'})     
            }
        
# class gmail_form(ModelForm):
#    class Meta:
#        model = cust
#        fields = ['email' , 'name'] 
