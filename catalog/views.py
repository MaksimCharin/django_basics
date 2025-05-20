from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products_list.html', context)


def product_detail(request, pk):
    product_detail = Product.objects.get(pk=pk)
    context = {
        'product_detail': product_detail,
    }
    return render(request, 'product_detail.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"{name}, Ваши данные отправлены!")
    return render(request, 'contacts.html')