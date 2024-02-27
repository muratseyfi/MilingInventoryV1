import django_filters
from django_filters import DateFilter, CharFilter, ModelChoiceFilter, BooleanFilter
from .models import *
from django import forms

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = DateFilter(field_name='created_at', lookup_expr='lte')
    status = BooleanFilter(field_name='status')
    product = ModelChoiceFilter(
        queryset=Product.objects.all(),
        empty_label="All Products",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    staff = ModelChoiceFilter(
        queryset=User.objects.all(),
        empty_label="All Staffs",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    customer = ModelChoiceFilter(
        queryset=Customer.objects.all(),
        empty_label="All Customers",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['product','staff', 'customer' ,'status', 'created_at', 'order_quantity']


class ProductFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = DateFilter(field_name='created_at', lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label="All Category",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['name','category', 'created_at']