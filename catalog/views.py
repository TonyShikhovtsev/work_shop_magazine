from django.shortcuts import render,  get_object_or_404, redirect
from catalog.models import Product
from catalog.forms import ProductForm

def home(request):
    product_list = Product.objects.all()
    if product_list:
        context = {
            'products': product_list
        }
    else:
        context = {
            'products': None
        }
    return render(request, 'catalog/home.html', context)


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


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'catalog/create_product.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)

    return render(request, 'catalog/edit_product.html', {'form': form, 'product': product})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('home')

    return render(request, 'catalog/delete_product.html', {'product': product})

