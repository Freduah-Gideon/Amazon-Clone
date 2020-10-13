from django.urls import path
from . import views
app_name = 'order'
urlpatterns = [
    path('cart-modification/', views.CartOptionsView.as_view(), name='modify-cart'),
    path('cart-update-modification/', views.CartQuantityModification.as_view(),
         name='cart-update-modification'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('custom_checkout/',views.UseCustomView.as_view(),name='custom_checkout'),
    path('r_s/<int:id>/', views.RemoveShippingAddress.as_view(),
         name='remove_shipping_address'),
    path('payment/<str:option>/', views.PAYMENT_VIEW.as_view(), name='payment')
]
