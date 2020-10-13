from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from products.models import Product
from .models import OrderItem, Order, Checkout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse
from .forms import CheckoutForm
# Create your views here.
import random
import string
def create_ref_code():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=20))

class CartOptionsView(LoginRequiredMixin, View):
    def get_object(self, request, **kwargs):
        response = {}
        try:
            product = Product.objects.get(
                id=self.request.POST.get('product-id'))
            return product
        except Product.DoesNotExist:
            messages.info(self.request, 'Item Cannot Be Found')
            return HttpResponseRedirect(reverse('order:cart'))

    def post(self, request, **kwargs):
        response = {}
        item = self.get_object(self.request.POST.get('product-id'))
        print(item)
        order_item, created = OrderItem.objects.get_or_create(
            user=self.request.user,
            item=item
        )
        order_item.quantity = int(self.request.POST.get('quantity'))
        order_item.save()
        order_filter = Order.objects.filter(
            user=self.request.user, is_ordered=False)

        if order_filter.exists():
            order = order_filter[0]
            if order.items.filter(item__id=item.id).exists():
                if item.in_stock > order_item.quantity:
                    order_item.quantity += 1
                    order_item.save()
                    messages.info(
                        self.request, 'Item Quantity Has Been Updated')
                    return HttpResponseRedirect(reverse('order:cart'))
                    # response['status'] = 'Item Quantity Has Been Updated'
                    # return JsonResponse(response)
                else:
                    messages.info(
                        self.request, 'Item Quantity Cannot Exceed In Stock Quantity')
                    return HttpResponseRedirect(reverse('order:cart'))
                    # response['status'] = 'Item Quantity Cannot Exceed In Stock Quantity'
                    # return JsonResponse(response)
            else:
                order.items.add(order_item)
                order.save()
                messages.info(self.request, 'Item Has Been Added To Cart')
                return HttpResponseRedirect(reverse('order:cart'))
                # response['status'] = 'Item Has Been Added To Cart'
                # return JsonResponse(response)
        else:
            order = Order.objects.create(
                user=self.request.user,
            )
            order.items.add(order_item)
            order.save()
            messages.info(self.request, 'Item Has Been Added To Cart')
            return HttpResponseRedirect(reverse('order:cart'))
            # response['status'] = 'Item Has Been Added To Cart'
            # return JsonResponse(response)

    def delete(self, request, **kwargs):
        item = self.get_object(self.request.POST.get('product-id'))
        response = {}
        try:
            order_item = OrderItem.objects.get(
                item=item, user=self.request.user)
            order_item.delete()
            response['status':'Item Removed From Cart']
            return JsonResponse(response)
        except OrderItem.DoesNotExist:
            response['status':'Item Was Not In Cart']
            return JsonResponse(response)

    def put(self, request, **kwargs):
        item = self.get_object(self.request.POST.get('item'))
        item.quantity += int(self.request.POST.get('quantity'))
        item.save()
        print(self.request.get_full_path())
        messages.info(self.request, 'Item Quantity Updated')
        return HttpResponse('Ohk')
        # return HttpResponseRedirect(reverse(''))

class CartQuantityModification(LoginRequiredMixin, View):
    def get_absolute_url(self, request, **kwargs):
        order = Order.objects.get(user=self.request.user, is_ordered=False)
        if order.items.all().count() >= 1:
            return HttpResponseRedirect(reverse('order:cart'))
        else:
            return HttpResponseRedirect(reverse('product:home'))

    def post(self, request, **kwargs):
        try:
            quantity = self.request.POST.get('quantity')
            order_item_id = self.request.POST.get('item')
            order_item = OrderItem.objects.get(
                user=self.request.user,
                id=order_item_id
            )
            item_filtering = Product.objects.filter(id=order_item.item.id)
            if item_filtering.exists():
                stock_quantity = item_filtering[0].in_stock
                if int(stock_quantity) < int(quantity):
                    messages.info(self.request, 'Quantity Exceeds Stock')
                    return self.get_absolute_url(self)
                elif int(quantity) == 0:
                    messages.info(self.request, 'Item Removed')
                    order_item.delete()
                    return self.get_absolute_url(self)
                else:
                    order_item.quantity = quantity
                    order_item.save()
                    return self.get_absolute_url(self)

            else:
                messages.info(
                    self.request, 'Product Might Have Been Removed')
                return self.get_absolute_url(self)
        except OrderItem.DoesNotExist:
            messages.info(self.request, 'This Item Does Not Exist Anymore')
            return self.get_absolute_url(self)
        # except:
        #     messages.info(self.request, 'An Error Occured, Please Try Again')
        #     return self.get_absolute_url(self)


class CartView(LoginRequiredMixin, View):

    def get(self, request, **kwargs):
        try:
            cart_content = Order.objects.get(
                user=self.request.user,
                is_ordered=False,
                is_payed=False
            )
            context = {
                'cart': cart_content
            }
            return render(self.request, 'cart.html', context)
        except Order.DoesNotExist:
            return render(self.request, 'cart.html')


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        response = {}
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            if self.request.is_ajax():
                print('Request Is Ajax')
                '''
                    try:
                        checkout = Checkout.objects.get(
                            user=self.request.user, id=self.kwargs.get('id'))
                        order.shipping_address = checkout
                        # order.save()
                        messages.info(
                            self.request, 'You Have Been Redirected To Your Payment Page')
                        if checkout.payment_option == 'm':
                            response['redirect':reverse(
                                'order:payment', args=('m'))]
                            return JsonResponse(response)
                        elif checkout.payment_option == 'v':
                            response['redirect':reverse(
                                'order:payment', args=('v'))]
                            print(response['redirect'])
                            return JsonResponse(response)
                        elif checkout.payment_option == 't':
                            response['redirect':reverse(
                                'order:payment', args=('t'))]
                            return JsonResponse(response)
                        else:
                            messages.info(
                                self.request, 'You"ve Fucked Up Your Payment')
                            return self.get(self)
                    except Checkout.DoesNotExist:
                        response['error':'CheckOut Details Does Not Exist']
                        return JsonResponse(response)
                    '''
            if order.items.all().count() == 0:
                messages.info(
                    self.request, 'You Have No Items To Checkout Please Start Shopping')
                return HttpResponseRedirect(reverse('product:home'))
            else:
                context = {
                    'form': CheckoutForm(),
                    'shipping_addresses': Checkout.objects.filter(user=self.request.user, is_saved=True).all()
                }
                return render(self.request, 'checkout.html', context)
        except Order.DoesNotExist:
            messages.info(
                self.request, 'You Have No Active Orders, Please Start Shopping')
            return HttpResponseRedirect(reverse('product:home'))

    def post(self, request, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)

            if order.items.all().count() == 0:
                messages.info(
                    self.request, 'You Have No Items To Checkout Please Start Shopping')
                return HttpResponseRedirect(reverse('product:home'))
            else:
                form = CheckoutForm(self.request.POST or None)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.user = self.request.user
                    # new_form.save()
                    # order.shipping_address = new_form
                    # order.save()
                    messages.info(
                        self.request, 'You Have Been Redirected To Your Payment Page')
                    if new_form.payment_option == 'm':
                        return HttpResponseRedirect(reverse('order:payment', args=('m')))
                    elif new_form.payment_option == 'v':
                        return HttpResponseRedirect(reverse('order:payment', args=('v')))
                    elif new_form.payment_option == 't':
                        return HttpResponseRedirect(reverse('order:payment', args=('t')))
                    else:
                        messages.info(
                            self.request, 'You"ve Fucked Up Your Payment')
                        return self.get(self)
        except Order.DoesNotExist:
            messages.info(
                self.request, 'You Have No Active Orders, Please Start Shopping')
            return HttpResponseRedirect(reverse('product:home'))

class UseCustomView(LoginRequiredMixin, View):
    http_method_names = ['post']
    def post(self, request):
        response = {}
        try:
            id = self.request.POST.get('id')
            checkout = Checkout.objects.get(id=id, user=self.request.user)
            try:
                order = Order.objects.get(user=self.request.user,is_ordered=False)
                order.shipping_address = checkout
                order.save()
                if checkout.payment_option == 'm':
                    response['redirect']  = reverse('order:payment', args=('m'))
                elif checkout.payment_option == 'v':
                    response['redirect'] = reverse('order:payment', args=('v'))
                else:
                    response['redirect'] = reverse('order:payment', args=('t'))
                return JsonResponse(response)
            except Order.DoesNotExist:
                response['redirect'] = reverse('product:home')
        except Checkout.DoesNotExist:
            messages.info(self.request,'This Shipping Address Has Been Deleted')
            response['redirect'] = reverse('order:checout')
            return JsonResponse(response)


class RemoveShippingAddress(LoginRequiredMixin, View):
    # http_method_names = ['delete']
    def get(self, request, id):
        try:
            addr = Checkout.objects.get(id=id, user=self.request.user)
            # addr.delete()
            response = {'OK': 'OK'}
            return JsonResponse(response)
        except Checkout.DoesNotExist:
            response = {'ERROR': 'ERROR'}
            return JsonResponse(response)


class PAYMENT_VIEW(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        if self.kwargs.get('option') == 'm'.lower():
            return HttpResponse('Momo')
        elif self.kwargs.get('option') == 'v'.lower():
            return HttpResponse('Vodafone')
        elif self.kwargs.get('option') == 't'.lower():
            return HttpResponse('Tigo Cash')
        else:
            return HttpResponse('Invalid Payment Option Provided')

    def post(self, request, **kwargs):
        pass
