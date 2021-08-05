from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *


def all_restaurants(request):
    context = {}
    return render(request, 'all_restaurants.html', context)


def my_products(request):
    context = {}
    if(request.GET.get('DeleteButton')):
        this_name=request.GET.get('DeleteButton')
        print("COCOS", this_name)
    return render(request, 'my_products.html', context)


def menu(request, restaurant_name, username):
    current_restaurant = Restaurant.objects.filter(username=restaurant_name).first()
    products = Product.objects.filter(restaurant=current_restaurant)
    user = Customer.objects.filter(username=username).first()
    context = {'restaurant': current_restaurant, 'products': products, 'current_user': user}
    return render(request, 'menu.html', context)


def customer_login(request):
    context = {}
    if request.method == 'POST':
        this_username = request.POST.get('username')
        this_password = request.POST.get('password')
        user = Customer.objects.filter(username=this_username, password=this_password)
        if user.exists():
            return render(request, 'all_restaurants.html', {
                'current_user': user.first(),
                'restaurants': Restaurant.objects.all(),
            })
    return render(request, 'customer_login.html', context)

def restaurant_login(request):
    context = {}
    if request.GET.get('DeleteButton'):
        Product.objects.filter(id=request.GET.get('DeleteButton')).delete()
    if request.method == 'POST':
        this_username = request.POST.get('username')
        this_password = request.POST.get('password')
        user = Restaurant.objects.filter(username=this_username, password=this_password)
        if user.exists():
            return render(request, 'my_products.html', {
                'user': user.first(),
                'products': Product.objects.filter(restaurant=user.first())
            })
    return render(request, 'restaurant_login.html', context)


def customer_logout(request):
    context = {}
    return render(request, 'customer_login.html', context)


def restaurant_logout(request):
    context = {}
    return render(request, 'restaurant_login.html', context)


def splitscreen(request):
    print(request)
    return render(request, 'splitscreen.html', {
    })

def customer_register(request):
    form = RegisterCustomerForm()
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'customer_register.html', context)


def restaurant_register(request):
    form = RegisterRestaurantForm()
    if request.method == 'POST':
        form = RegisterRestaurantForm(request.POST)
        if form.is_valid():
            print('VALIIIIIIIIIIID')
            form.save()
    context = {'form': form}
    return render(request, 'restaurant_register.html', context)

def addproduct(request, restaurant_name):
    current_restaurant = Restaurant.objects.filter(username=restaurant_name).first()
    if request.method == 'POST':
        this_name = request.POST.get('name')
        this_price = float(request.POST.get('price'))
        this_restaurant_name = request.POST.get('restaurant')
        Product.objects.create(name=this_name, price=this_price, image=request.POST.get('image'), restaurant=Restaurant.objects.filter(username=this_restaurant_name).first())
        print("COCOS adaugat")
    context = {'restaurant': current_restaurant}
    return render(request, 'add_product.html', context)

def cart(request, username):
    user = Customer.objects.filter(username=username).first()
    context = {'user': user}
    return render(request, 'cart.html', context)
