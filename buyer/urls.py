from django.urls import path
from .views import *

urlpatterns = [
    path('compair/', compair, name='compair'),
    path('components/', components, name='components'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('forgetpass/', forgetpass, name='forgetpass'),
    path('index/', index, name='index'),
    path('legel_notice/', legal_notice, name='legel_notice'),
    path('login/',login, name='login'),
    path('normal/', normal, name='normal'),
    path('product_details/', product_details, name='product_details'),
    path('product_summary/', product_summary, name='product_summary'),
    path('products/', products, name='products' ),
    path('register/', register, name='register'),
    path('special_offer/',special_offer, name='special_offer' ),
    path('tac/', tac, name='tac'),
    path('otp/' ,otp, name='otp' ),
    path('header/',header,name='header'),
    path('logout/',logout,name='logout'),
    path('add_to_cart/<int:pk>',add_to_cart,name='add_to_cart'),
    path('del_cart_item/<int:c_item>',del_cart_item,name='del_cart_item'),
    path('product_summary/paymenthandler/', paymenthandler, name='paymenthandler'),



    path('add_row/',add_row, name='add_jenil')
    

    

]