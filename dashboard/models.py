from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}'

CUSTOMERTYPE = (
    ('Individual','Individual'),
    ('Company','Company'),
    ('Government','Government'),
)

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    customer_type = models.CharField(max_length=20, choices= CUSTOMERTYPE, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=200, null=True)
    representative =models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Customer'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #customer = models.CharField(max_length=200, null=True, default='1')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
    

class Supplier(models.Model):
    name = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=200, null=True)
    representative =models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Supplier'

    def __str__(self):
        return f'{self.name}'