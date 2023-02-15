from django.contrib import admin

from .models import cust
from .models import product

#////////////////////////////

admin.site.register (cust)
admin.site.register (product)
# Register your models here.
