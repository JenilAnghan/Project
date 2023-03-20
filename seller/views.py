from django.shortcuts import render,redirect 
from random import randrange
from django.conf import settings
from .models import *
from buyer.models import *
from django.core.mail import send_mail

# Create your views here.
def seller_blank_pages(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_blank_pages.html',{'seller_data': seller_obj})

def seller_bootstrap_alert(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_alert.html',{'seller_data': seller_obj})

def seller_bootstrap_badge(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_badge.html',{'seller_data': seller_obj})

def seller_bootstrap_breadcrumb(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_breadcrumb.html',{'seller_data': seller_obj})

def seller_bootstrap_card(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_card.html',{'seller_data': seller_obj})

def seller_bootstrap_carousel(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_carousel.html',{'seller_data': seller_obj})

def seller_bootstrap_dropdown(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_dropdown.html',{'seller_data': seller_obj})

def seller_bootstrap_list_group(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_list_group.html',{'seller_data': seller_obj})

def seller_bootstrap_modal(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_modal.html',{'seller_data': seller_obj})

def seller_bootstrap_nav(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_nav.html',{'seller_data': seller_obj})

def seller_bootstrap_pagination(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_pagination.html',{'seller_data': seller_obj})

def seller_bootstrap_progress(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_progress.html',{'seller_data': seller_obj})

def seller_bootstrap_spinner(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_bootstrap_spinner.html',{'seller_data': seller_obj})

def seller_buttons(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_buttons.html',{'seller_data': seller_obj})

def seller_chart_apexcharts(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_chart_apexcharts.html',{'seller_data': seller_obj})

def seller_chart_chartjs(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_chart_chartjs.html',{'seller_data': seller_obj})

def seller_chatboxs(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'sellerseller_chatboxs_forms_checkbox.html',{'seller_data': seller_obj})

def seller_component_avatar(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_component_avatar.html',{'seller_data': seller_obj})

def seller_component_hero(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_component_hero.html',{'seller_data': seller_obj})

def seller_component_sweet_alert(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_component_sweet_alert.html',{'seller_data': seller_obj})

def seller_component_toastify(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_foseller_component_toastifyrms_checkbox.html',{'seller_data': seller_obj})

def seller_credits(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_credits.html',{'seller_data': seller_obj})

def seller_default(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_default.html',{'seller_data': seller_obj})

def seller_editor(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_editor.html.',{'seller_data': seller_obj})

def seller_email(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_default.html',{'seller_email': seller_obj})

def seller_errors_403(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_errors_403.html',{'seller_data': seller_obj})

def seller_errors_404(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_errors_404.html',{'seller_data': seller_obj})

def seller_errors_500(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_errors_500.html',{'seller_data': seller_obj})

def seller_errors_503(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_errors_503.html',{'seller_data': seller_obj})

def seller_forgot_password(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_forgot_password.html',{'seller_data': seller_obj})

def seller_forms_checkbox(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_forms_checkbox.html',{'seller_data': seller_obj})

def seller_icons_boostrap(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_forms_checkbox.html',{'seller_data': seller_obj})

def seller_forms_validation(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_forms_validation.html',{'seller_data': seller_obj})

def seller_index(request):
    try:
        s_obj = Seller.objects.get(email= request.session['seller_email'])
        return render(request, 'seller_index.html', {'seller_data':s_obj})
    except:
        return render(request, 'seller_login.html')


def seller_pricing(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_pricing.html',{'seller_data': seller_obj})

def seller_radio(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_radio.html',{'seller_data': seller_obj})

def seller_register(request):
    if request.method == 'GET':
        return render(request, 'seller_register.html')
    else:
        try:
            Buyer.objects.get(email = request.POST['email'])
            return render(request, 'seller_register.html', {'msg': 'Email Is Already registered!!'})
        except:
            if request.POST['password'] == request.POST['repassword']:
                s = "Ecommerce Registration!!"
                global user_data
                user_data = [request.POST['full_name'], request.POST['email'], request.POST['password']]
                global c_otp
                c_otp = randrange(1000,9999)
                m = f'Hello User!!\nYour OTP is {c_otp}'
                f = settings.EMAIL_HOST_USER
                r = [request.POST['email']]
                send_mail(s, m, f, r)
                return render(request, 'seller_otp.html', {'msg': 'Check Your MailBox'})
            else:
                return render(request, 'seller_register.html', {'msg': 'Both Passwords do not match!!'})


def seller_otp(request):
    try:
        if str(c_otp) == request.POST['otp']:
            Buyer.objects.create(
                full_name = user_data[0],
                email = user_data[1],
                password = user_data[2],
                # repassword = user.data[3]
            )
        else:
            return render(request,'seller_register.html',{'msg':'account created successfully !!!'})

    except:
        return render(request,'seller_otp.html',{'msg':'wrong otp enter again'})

def seller_reset_password(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_reset_password.html',{'seller_data': seller_obj})


def seller_layout_top_navigation(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_layout_top_navigation.html',{'seller_data': seller_obj})

def seller_login(request):
    if request.method == 'POST':
        try:
            seller_obj = Seller.objects.get(email = request.POST['email'])
            if request.POST['password'] == seller_obj.password:
                request.session['seller_email'] = request.POST['email']
                return render(request, 'seller_profile.html',{'seller_data': seller_obj})
            else:
                return render(request, 'seller_login.html', {'msg': 'Wrong Password!!'})

        except:
            return render(request, 'seller_login.html', {'msg':'Email is Not Registered!!'})

    else:
        return render(request, 'seller_login.html')

def seller_header(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_header.html',{'seller_data': seller_obj})

def seller_widgets_email(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_widgets_email.html',{'seller_data': seller_obj})

def seller_logout(request):
    del request.session['seller_email']
    return redirect('seller_login')

def seller_profile(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    if request.method == 'GET':
        return render(request,'seller_profile.html',{'seller_data':seller_obj})

    else:
        seller_obj.full_name = request.POST['full_name']
        seller_obj.address = request.POST['address']
        seller_obj.gst_no = request.POST['gst_no']
        try:

            seller_obj.pic = request.FILES['pic']

            seller_obj.save() # database ma change karva mate call karvo pade

        except:
             seller_obj.save() # database ma change karva mate call karvo pade

        return redirect('seller_profile')


def seller_add_product(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    if request.method == 'GET':
        return render(request,'seller_add_product.html',{'seller_data':seller_obj})

    else:
         # ek product dp ma add karishu

         Product.objects.create(
            product_name = request.POST['product_name'],
            des = request.POST['des'],
            price = request.POST['price'],
            product_stock = request.POST['product_stock'],
            pic = request.FILES['pic'],
            seller = seller_obj
        ) 
         
         return redirect('seller_add_product')


def my_product(request):
    s_obj = Seller.objects.get(email = request.session['seller_email'])
    my_pros = Product.objects.filter(seller = s_obj)
    # print(my_pros)
    return render(request,'my_product.html',{ 'seller_data':s_obj,'my_all_product':my_pros})

def product_delete(request , pk):
    p_obj = Product.objects.get(id = pk)
    p_obj.delete()
    return redirect('my_product')

def product_edit(request, pk):
    p_obj = Product.objects.get(id = pk)
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    if request.method == 'GET':
        return render(request, 'edit_product.html', {'seller_data':seller_obj, 'product_data': p_obj})

    else:
        p_obj.product_name = request.POST['product_name']
        p_obj.des = request.POST['des']
        p_obj.price = request.POST['price']
        p_obj.product_stock = request.POST['product_stock']
        try:  
            p_obj.pic = request.FILES['pic']
            p_obj.save()
            return render(request, 'edit_product.html', {'seller_data':seller_obj, 'product_data': p_obj})
   
        except:
        
            return redirect(request, 'my_product.html')
   

    
    
