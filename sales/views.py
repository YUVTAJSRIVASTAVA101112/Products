from venv import create
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render
from sales.models import Product 
from .models import Cart, CartItem
# from .forms import ContactForm
from django.contrib.auth.models import User # type: ignore
# from .forms import UserForm
from .models import MomDaughters



def home(request):
    return render(request,'home.html')

def contact_us(request):
    return render(request,'contact_us.html')

def about_us(request):
    return render(request,'about_us.html')

def terms_condition(request):
    return render(request,'terms_condition.html')





# def user_logout(request):
#     logout(request)
#     return redirect('/login_view')


def shop_now1(request):
    return render(request,'shop_now1.html')

def shop_now2(request):
    return render(request,'shop_now2.html')

def shop_now3(request):
    return render(request,'shop_now3.html')

def shop_now4(request):
    return render(request,'shop_now4.html')

def shop_now5(request):
    return render(request,'shop_now5.html')


def product1(request):
    return render(request,'product1.html')

def product2(request):
    return render(request,'product2.html')

def product3(request):
    return render(request,'product3.html')

def product4(request):
    return render(request,'product4.html')

def product5(request):
    return render(request,'product5.html')

def ethnic(request):
    return render(request,'ethnic.html')

def women_attire(request):
    return render(request,'women_attire.html')

def details1(request):
    return render(request,'details1.html')

def details2(request):
    return render(request,'details2.html')

def details3(request):
    return render(request,'details3.html')

def details4(request):
    return render(request,'details4.html')

def details5(request):
    return render(request,'details5.html')

def details6(request):
    return render(request,'details6.html')

def first_bd(request):
    return render(request,'first_bd.html')

def casual(request):
    return render(request,'casual.html')

def ethnic(request):
    return render(request,'ethnic.html')

def mom_daughter(request):
    return render(request,'mom_daughter.html')

def party(request):
    return render(request,'party.html')

def accessories(request):
    return render(request,'accessories.html')

from django.shortcuts import render

def rent_studio_spaces(request):
    return render(request, 'rent_studio_spaces.html')



# contact form

# from django.shortcuts import render
# from django.http import JsonResponse
# from .forms import ContactForm

# def submit_form(request):
#     if request.method == 'POST' and request.is_ajax():
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
    
# login form



def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/')
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})

#sabmit form

def submit_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Form submitted successfully!"})
    else:
        form = UserForm()
    return render(request, 'your_template.html', {'form': form})

# product list 

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# gown list

from .models import Gown

def gown_list(request):
    gown = Gown.objects.all()
    return render(request, 'gown_list.html', {'gown': gown})

# accessories

from .models import Accessories

def accessories(request):
    access = Accessories.objects.all()
    return render(request,'accessories.html', {'access': access})


# 1st birthday

from .models import Birthdays

def birth_day(request):
    birth = Birthdays.objects.all()
    return render(request,'birthday_list.html', {'birth': birth})

# casual 

from .models import Casuals

def casual_list(request):
    casual = Casuals.objects.all()
    return render(request,'casual.html', {'casual': casual})

# ethnic

from .models import Ethnics

def ethnic_list(request):
    ethnic = Ethnics.objects.all()
    return render(request,'ethnic.html', {'ethnic': ethnic})

# party
from .models import Parties

def party_view(request):
    party = Parties.objects.all()
    return render(request, 'party.html', {'parties': party})




# mom-daughter


def mom_daughter_view(request):
    mom_daughter = MomDaughters.objects.all()
    return render(request, 'mom_daughter.html', {'mom_daughter': mom_daughter})

#cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart/cart_detail.html', {'cart': cart})

#submit form
# def submit_form(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({"message": "Form submitted successfully!"})
#     else:
#         form = ContactForm()
#     return render(request, 'your_template.html', {'form': form})