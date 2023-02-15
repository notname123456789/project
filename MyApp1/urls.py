from django.urls import path
from . import views
urlpatterns = [  
    path ('', views.hi , name = 'hi'),
    path ('index/' , views.game.as_view() , name = 'index' ),
    path ('products/' , views.products , name = 'products'),
    path ('products/<int:pk>' , views.products , name = 'products'),
    path ('product_desp/<int:pk>' , views.dep.as_view() , name = 'product_desp'),
    path ('basket/' , views.bsk , name = 'basket')
]
