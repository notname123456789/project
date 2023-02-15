from django.forms import ModelForm , TextInput , EmailInput , PasswordInput
from .models import cust
class customers(ModelForm):
    class Meta:
        model = cust
        fields = ['name','surname','email','password']

        widgets = {
            "name": TextInput (attrs = { 'placeholder': 'имя'}),
            "surname": TextInput (attrs = { 'placeholder': 'фамилия'}),
            "email": EmailInput (attrs = { 'placeholder': 'почта' , 'type' : 'email'}),
            "password": PasswordInput (attrs = { 'placeholder': 'пароль' , 'type' : 'password'})
            }
        
# class gmail_form(ModelForm):
#    class Meta:
#        model = cust
#        fields = ['email' , 'name'] 
