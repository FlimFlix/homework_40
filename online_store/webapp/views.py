from django.shortcuts import render, redirect
from webapp.models import Product
from django.http import Http404


def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main.html', context)


def product_view(request, product_id):
    print(request.GET)
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'product': product
    }
    return render(request, 'view.html', context)


def create_view(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        cost = request.POST.get('cost')
        product = Product.objects.create(name=name, description=description, cost=cost)
        return redirect('product', product_id=product.pk)


def about_company_view(request):
    return render(request, 'about_company.html')


def contacts_view(request):
    return render(request, 'contacts.html')
