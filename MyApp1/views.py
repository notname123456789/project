from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import product
from datetime import datetime
from .forms import customers
from .models import cust 
from django.views.generic import DetailView 
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import JsonResponse
from django.forms.models import model_to_dict
current_datetime = datetime.now()
form = customers()
error = ''
data = {
     'obj' :
         {
     'time' : current_datetime.date ,
     'text' : "текст из data",
     'form' : form,
     'error' : error ,
     
         }
    }

bsk_data = [] ;
a = 10;
def send (x):
      send_mail (
          'надеюсь эта хрень работает',
          'сраный джанго',
          'notmypochta@gmail.com',
          [x],
          fail_silently=False ,          
      )

def hi (x):   

    if x.method == 'POST' :
        form = customers(x.POST)
        if form.is_valid():            
            #some = 
            form.save()
            send(form.instance.email)
            #return JsonResponse ({'output' : model_to_dict (some)} , status = 200)
        else :
            error = 'аааааааааа'  
    if x.GET.get ('spam'):
        print ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
            
    form = customers()        
    return render (x , 'MyApp1/Kolobok.html' , data)

class game (TemplateView):
    template_name = 'MyApp1/index.html'

    def func ():
      print ("it works")

def products (x , pk): 

    sum_of_onsite = 3 ;
    pag_num = x.GET.get('pk') ; print(pk)
    notepk = pk; t = notepk * sum_of_onsite; f = t-sum_of_onsite;
    #___________________________________________________________

    sum_of_obj = product.objects.count() ; print (sum_of_obj)     
    not_int_sop = sum_of_obj / sum_of_onsite; print (not_int_sop)
    sum_of_pag = int(sum_of_obj / sum_of_onsite) ; print (sum_of_pag)
    if not_int_sop > sum_of_pag :
        print("sss"); sum_of_pag += 1; print (sum_of_pag) ;

    arr = list(range(1, sum_of_pag+1 ))
    data_of_this_fc = {
        'sum_of_pag' : sum_of_pag ,
        'sum_of_obj' : sum_of_obj ,
        'arr' : arr
        }
    #_____________________________________________________________
    # if x.GET.get ('to_basket'):    
       # global a
       # print (a);
       # z = x.GET.get ;        
       # print (z);                       
       #        
    #_____________________________________________________________
    global bsk_data
    z = x.POST.get ('to_basket');
    if 'to_basket' in x.POST:          
        print ("this is -", z , "???");
        obj = product.objects.all();
        for el in obj :
            print ("lol - " , el.id , "= не=" , z);
            if int(z) == int (el.id) :
                print ("lololooo")
                bsk_data.append (el);
    print ("bsk_data ---"); print (bsk_data);
    print ("all objects from models ---"); print (product.objects.all());
    print (z);
    #_____________________________________________________________
    product_on_site = product.objects.order_by('price')[f:t]
    return render (x , 'MyApp1/products.html' , {'product_on_site' : product_on_site , 'data' : data_of_this_fc})

class dep (DetailView):
    model = product
    template_name = 'MyApp1/product_desp.html'
    context_object_name = 'pr'

def bsk (x):
    return render (x , 'MyApp1/basket.html' , {'pib' : bsk_data})


# Create your views here.
