from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Product
from .forms import ProductFilterForm

def index(request):
    Product.objects.prefetch_related(Prefetch('productimage_set'))
    
    products = Product.objects.all().order_by('name')
    if request.GET.get('sort')=='price':
      products = products.order_by('price')
    elif request.GET.get('sort')=='name':
      products = products.order_by('name')
    elif request.GET.get('sort')=='minimum_age_appropriate':
      products = products.order_by('minimum_age_appropriate')

      
    form = ProductFilterForm(request.GET)


    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    name_search = request.GET.get('name_search')
    if name_search:
        products = products.filter(name__icontains=name_search)
    elif min_price: 
        products = products.filter(price__gt=min_price)
    elif max_price:
        products = products.filter(price__lt=max_price)

  
    context = {'products': products, 'form': form}
    return render(request, 'products/index.html', context)

def show(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    context = { 'product':p }
    return render(request, 'products/show.html', context)
    
