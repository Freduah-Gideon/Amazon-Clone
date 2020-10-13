from django.contrib import admin
from .models import Product, Features

class OrderAdmin(admin.ModelAdmin):
    list_filter = ['product']
    
# Register your models here.
admin.site.register(Product)
admin.site.register(Features)