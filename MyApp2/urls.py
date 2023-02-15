from django.urls import path
from . import views
urlpatterns = [  
    path ('' , views.se , name = 'second'),
    path('<int:pk>' , views.se , name = 'second'),
    path ('pvy/' , views.pny , name = 'pvy'),
    path ('pvn/' , views.pnv , name = 'pvn'),
    path ('np/' , views.new_news , name = 'np'),
    path ('pr/' , views.pvf , name = 'pr'),
    path ('rt/' , views.rt , name = 'rt'),
    path('rt_plus/<int:pk>' , views.rt_plus.as_view() , name = 'rt_plus'),
]

