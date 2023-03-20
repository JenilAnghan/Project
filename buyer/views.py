from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from random import randrange
from django.conf import settings
from django.http import HttpResponse
from seller.models import *
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# Create your views here.


def compair(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'index.html', {'user_data': buyer_row})
    except:
        return render(request, 'index.html',)


def components(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'components.html', {'user_data': buyer_row})
    except:
        return render(request, 'components.html')


def contact(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'contact.html', {'user_data': buyer_row})
    except:

        return render(request, 'contact.html')


def faq(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'faq.html', {'user_data': buyer_row})
    except:
        return render(request, 'faq.html',)


def forgetpass(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'forgetpass.html', {'user_data': buyer_row})
    except:
        return render(request, 'forgetpass.html')


def index(request):
    try:

        all_pros = Product.objects.all()

        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'index.html', {'user_data': buyer_row, 'all_products': all_pros})
    except:
        return render(request, 'index.html')


def legal_notice(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'legal_notice.html', {'user_data': buyer_row})
    except:
        return render(request, 'legal_notice.html')


def normal(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'normal.html', {'user_data': buyer_row})
    except:
        return render(request, 'normal.html')


def otp(request):
    return render(request, 'otp.html')


def product_details(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'product_details.html', {'user_data': buyer_row})
    except:
        return render(request, 'product_details.html')


def products(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'products.html', {'user_data': buyer_row})
    except:
        return render(request, 'products.html')


def register(request):
    return render(request, 'register.html')


def special_offer(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'special_offer.html', {'user_data': buyer_row})
    except:
        return render(request, 'special_offer.html')


def tac(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'tac.html', {'user_data': buyer_row})
    except:
        return render(request, 'tac.html')


def add_row(request):
    Buyer.objects.create(
        email='jenil@gmail.com',
        first_name='jenil',
        last_name='Patel',
        password='@sjenil56788',
        address='Dabholi,surat',
        mobile='9056748780'
    )
    return render(request, 'success.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        try:
            Buyer.objects.get(email=request.POST['email'])
            return render(request, 'register.html', {'msg': 'Email Is Already registered!!'})
        except:
            if request.POST['password'] == request.POST['repassword']:
                s = "Ecommerce Registration!!"
                global user_data
                user_data = [request.POST['first_name'],
                             request.POST['last_name'],
                             request.POST['email'],
                             request.POST['password']]
                global c_otp
                c_otp = randrange(1000, 9999)
                m = f'Hello User!!\nYour OTP is {c_otp}'
                f = settings.EMAIL_HOST_USER
                r = [request.POST['email']]
                send_mail(s, m, f, r)
                return render(request, 'otp.html', {'msg': 'Check Your MailBox'})
            else:
                return render(request, 'register.html', {'msg': 'Both Passwords do not match!!'})


def otp(request):

    if str(c_otp) == request.POST['otp']:
        Buyer.objects.create(
            first_name=user_data[0],
            last_name=user_data[1],
            email=user_data[2],
            password=user_data[3]
        )
        return render(request, 'register.html', {'msg': 'Account created successfully!!'})
    else:
        return render(request, 'otp.html', {'msg': 'Wrong OTP enter again!!'})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            # email check thay che
            buyer_row = Buyer.objects.get(email=request.POST['email'])

            # password check thay chhe
            # request.POST['password'] ###aa password tame login page ma enter karyo hase
            # buyer_row.password ###aa password database wado chhe
            if request.POST['password'] == buyer_row.password:
                # password sacho enter karyo chhe
                # login thai gayu/ session naam na glass ma email(je login na page par enter karyo hato e) mukaai gayo
                request.session['email'] = request.POST['email']
                return render(request, 'index.html', {'user_data': buyer_row})
            else:
                return render(request, 'login.html', {'msg': 'Wrong Password!!'})

        except:
            # jyare email madyo nathi
            return render(request, 'login.html', {'msg': 'email is not registered!!'})


def logout(request):
    del request.session['email']
    return redirect('index')


def header(request):
    return render(request, 'header.html')


def add_to_cart(request, pk):
    p_obj = Product.objects.get(id=pk)
    b1 = Buyer.objects.get(email=request.session['email'])
    Cart.objects.create(
        product_name=p_obj.product_name,
        price=p_obj.price,
        pic=p_obj.pic,
        buyer=b1
    )
    return redirect('index')


def product_summary(request):
    u1 = Buyer.objects.get(email=request.session['email'])
    # global c_list
    c_list = Cart.objects.filter(buyer=u1)
    global t_amount
    t_amount = 0
    for i in c_list:
        t_amount += i.price

    # for i in c_list:
    #      t_amount -= i.price

    # payment nu button jivit karva mate  no code

    currency = 'INR'
    amount = t_amount * 100 
    if t_amount==0:
        t_amount+=10 # Rs. 200
        return redirect('index')

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    context.update(
        {'user_data': u1, 'my_cart_data': c_list, 't_amount': t_amount})

    return render(request, 'product_summary.html', context=context)


def del_cart_item(request, c_item):
    c_obj = Cart.objects.get(id=c_item)
    c_obj.delete()
    return redirect('product_summary')


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
        # if(1):

            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = t_amount * 100
                try:
                # if(1):
                    razorpay_client.payment.capture(payment_id, amount)
                    session_user = Buyer.objects.get(email=request.session['email'])
                    c_obj = Cart.objects.filter(buyer=session_user)
                    for i in c_obj:
                        i.delete()

                    return render(request, 'paymentsuccess.html')
                except:
                # else:
                    return render(request, 'paymentfail.html')
            else:    
                return render(request, 'paymentfail.html')
        except:
        # else:

        # if we don't find the required parameters in POST data
         return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()
