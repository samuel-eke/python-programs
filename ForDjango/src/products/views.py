from django.shortcuts import render
from .models import Proudcts
from .forms import CreateProductform
# Create your views here.

def product_detail_view(request):
    obj = Proudcts.objects.get(id=3)
    context = {'object': obj,
    }
    return render (request, "product/detail.html", context)

def prod2 (request):
    obj = Proudcts.objects.get(id=4)
    context = {"object": obj,

    }
    return render(request, "product/product2.html", context)

def product_create_new (request):
    form = CreateProductform (request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateProductform()
    
    context = {
        'form': form
    }
    return render (request, 'product/product_create.html', context)
