from django.urls import reverse_lazy
from .models import Product
from news.filters import ProductFilter
from .forms import ProductForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'products/product_edit.html'


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'products/product_edit.html'


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('product_list')