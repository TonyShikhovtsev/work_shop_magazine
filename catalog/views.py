from django.shortcuts import render,  get_object_or_404
from catalog.models import Product

def home(requests):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(requests, 'catalog/home.html', context)


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        print("{}, ({}) says: {}\n{}".format(name, email, subject, message))
    return render(requests, 'catalog/contacts.html')


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
