from products.models import Product
import django_filters
from django import forms
from .models import Post


class ProductFilter(django_filters.FilterSet):
   class Meta:
       model = Product
       fields = {
           'name': ['icontains'],
           'quantity': ['gt'],
           'price': [
               'lt',  
               'gt',  
           ],
       }

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название'
    )

    author = django_filters.CharFilter(
        field_name='author__user__username',
        lookup_expr='icontains',
        label='Имя автора'
    )

    created_at = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='date__gte',
        label='После даты',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'created_at']

