from django.shortcuts import render
from django.views.generic import View
from .models import Product
from django.http import HttpResponse
# Create your views here.
class HomeView(View):
    def get(self,request):
        wireless_query_set = Product.objects.filter(category='Electronics',sub_category='wireless').all()
        context = {
            'wireless':wireless_query_set
        }
        return render(self.request,'index.html',context)


class ProductDetailView(View):
    def get_object(self,request, **kwargs):
        try:
            product = Product.objects.get(id=self.kwargs.get('id'))
            return product
        except Product.DoesNotExist:
            return HttpResponse('Product Does Not Exist')
    
    def get(self,request, **kwargs):
        product = self.get_object(self.kwargs.get('id'))
        context = {
            'product':product
        }
        return render(self.request,'detail.html',context)
        