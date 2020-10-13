from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
# Create your models here.
from products.models import Product

ORDER_STATUS = (
    ('Initiated','Initiated'),
    ('Pending','Pending'),
    ('Recieved','Recieved'),
    ('Processing','Processing'),
    ('Processed','Processed'),
    ('Shipping','Shipping'),
    ('Shipped','Shipped'),
    ('Packaging','Packaging'),
    ('Out For Delivery','Out For Delivery'),
    ('Delivered','Delivered'),
)

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_price(self):
        return f"{self.item.price * self.quantity}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    is_ordered = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Checkout', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=ORDER_STATUS, max_length=50, null=True,blank=True)
    coupon = models.ForeignKey('Coupon',on_delete=models.SET_NULL, null = True, blank=True)
    def total_order_price(self):
        total = 0
        for each_item in self.items.all():
            total += float(each_item.get_price())
            if self.coupon:
                total -= float(self.coupon.coupon_worth)
        return float(total)

PAYMENT_OPTIONS = (
    ('m', 'Mtn MoMo'),
    ('v', 'Vodafone Cash'),
    ('t', 'Tigo Cash')
)

class Coupon(models.Model):
    coupon_worth = models.DecimalField(decimal_places=2,max_digits=20)
    coupon_name = models.CharField(max_length=50)

class Checkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    country = CountryField(
        blank_label='(Select country)', null=True, blank=True)
    full_name = models.CharField(blank=False, null=False, max_length=50000)
    address_1 = models.CharField(blank=False, null=False, max_length=50000)
    address_2 = models.CharField(blank=True, null=True, max_length=50000)
    city = models.CharField(blank=False, null=False, max_length=50000)
    region = models.CharField(blank=False, null=False, max_length=50000)
    zip_code = models.CharField(blank=False, null=False, max_length=50000)
    phone = models.CharField(blank=True, null=True, max_length=50000)
    additional_info = models.TextField()
    payment_option = models.CharField(
        choices=PAYMENT_OPTIONS, max_length=50, null=True, blank=True)
    is_saved = models.BooleanField(default=False)

