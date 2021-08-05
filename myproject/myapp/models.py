from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = 'https://static8.depositphotos.com/1533030/997/v/950/depositphotos_9975181-stock-illustration-restaurant-icon.jpg'
        return url


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to='static/images')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
