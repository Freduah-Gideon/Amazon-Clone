from django.contrib import admin
from .models import OrderItem,Order,Checkout,Coupon
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','shipping_address','is_payed']

admin.site.register(OrderItem)
admin.site.register(Order,OrderAdmin)
admin.site.register(Checkout)
admin.site.register(Coupon)