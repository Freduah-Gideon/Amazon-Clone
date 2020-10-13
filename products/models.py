from django.db import models
from django.conf import settings
# Create your models here.
RATINGS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)
CATEGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('computers', 'Computers'),
)
SUB_CATEGORIES = (
    ('camera_and_photo','Camera & Photo'),
    ('laptops','Laptops'),
    ('wireless','wireless')
)


class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2,max_digits=10000000000000000)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2000,null=True,blank=True)
    sub_category = models.CharField(choices=SUB_CATEGORIES,max_length=2000,null=True,blank=True)
    in_stock = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()
    features = models.ManyToManyField('Features')

    def __str__(self):
        return f"{self.category}-------{self.name}"

class Features(models.Model):
    feature = models.CharField(max_length=100)