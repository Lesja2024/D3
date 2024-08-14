from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):

    model = Product
    ordering = 'name'
  #queryset = Product

    template_name = 'products.html'
    context_object_name = 'products'
    