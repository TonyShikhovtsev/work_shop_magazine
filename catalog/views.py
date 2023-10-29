from django.shortcuts import render
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

def info(requests):
    product = Product.objects.get(name='Айфон 18')
    context = {
        'product': product
    }
    return render(requests, 'catalog/info.html', context)

