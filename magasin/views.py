from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.cache import cache_page
from .models import Product

@cache_page(60 * 15) # cache for 15 minutes
def index(request):
    products = Product.objects.values_list('name', 'price')
    context = {'products': products}  
    return render(request, 'magasin/mesProduits.html', context)
