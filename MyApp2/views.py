from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import news # новости на странице
from .models import some_new # предложения из вне
from .forms import some_new_f # форма предложения из вне
from .models import student # люди
from .forms import st_form # регистрация
from .models import some_new_fs 
from .forms import st_new_f #???
from .models import rast # люди в рейтинг класса
#//////////////////////////////////////////////
import json
from django.shortcuts import *
from .forms import *
from .models import *
from django.template import RequestContext
#//////////////////////////////////////////////


def se (x , pk=1):            
    amount = 3;
    page = Paginator(news.objects.all() , amount).page(pk)
    ran = Paginator(news.objects.all() , amount).page_range

    return render (x , 'MyApp2/index.html' , {'product_on_site' : page ,'amount': ran })
#основная страница
#////////////////////////////////////////////////////////////////////////////////////

form = some_new_f()
def new_news (x) :

    if x.method == 'POST':
        form = some_new_f (x.POST)
        if form.is_valid():           
            form.save()     
    form = some_new_f()
    return render (x , 'MyApp2/np.html' , {'form_out' : form})

def pnv (x):

    if x.method == 'POST':
        form = some_new_f (x.POST)
        if form.is_valid():           
            form.save()     
    form = some_new_f()
    return render (x , 'MyApp2/pvn1.html' , {'form_out' : form}) #поменяй адреса

form_sn = st_new_f()
def pny (x):
    if x.method == 'POST':
        form_sn = st_new_f (x.POST)
        if form_sn.is_valid():           
            form_sn.save()     
    form_sn = st_new_f()

    return render (x , 'MyApp2/pvy.html' , {'form_out' : form_sn})

form_s = st_form()
def pvf (x) :
    if x.method == 'POST':        
        form_s = st_form (x.POST)
        students = student.objects.all();
        for el in students:
            #for el_f in x.POST:
            for el_s in el._meta.fields:
                #-
                print (el_s , "<---" , el._meta.fields)
                if el.name == x.POST['name'] and el.password == x.POST['password']:
                
            #if el == x.POST:
                    print ("ураааа");
                    #return redirect('../pvy') #ПОМЕНЯЙ АДРЕСА
                else: 
                    return redirect('../pvn') #ПОМЕНЯЙ АДРЕСА
    form_s = st_form()
    return render (x , 'MyApp2/privilege.html' , {'form_out' : form_s})    

def rt (x) :
    st_on_rt = rast.objects.all()
    return render (x , 'MyApp2/rating.html' , {'strt' : st_on_rt})

class rt_plus (DetailView):
    model = rast
    template_name = 'MyApp2/rt_plus.html'
    context_object_name = 'el'
#//////////////////////////////////////////////
# Create your views here.data = {'form_out' : some_new_f , 'model_out' : some_new , 'news' : news}
#print (el.name) ; print ("---") ; print (x.POST['name'])
#print (el.password) ; print ("---") ; print (x.POST['password'])
