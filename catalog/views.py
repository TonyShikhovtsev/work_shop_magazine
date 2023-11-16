from django.shortcuts import render,  get_object_or_404, redirect
from catalog.models import Product
from catalog.forms import ProductForm, VersionForm

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
    active_version = product.versions.filter(is_active=True).first()
    versions = product.versions.all()
    context = {
        'product': product,
        'active_version': active_version,
        'versions': versions,
    }
    return render(request, 'catalog/product.html', context)


def create_version(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            version = form.save(commit=False)
            version.product = product
            version.save()
            return redirect('product', pk=pk)
    else:
        form = VersionForm()

    return render(request, 'catalog/create_version.html', {'form': form, 'product': product})

def create_version(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            version = form.save(commit=False)
            version.product = product
            version.save()
            print("Version saved successfully!")
            return redirect('product', pk=pk)
        else:
            print("Form errors:", form.errors)
    else:
        form = VersionForm()

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'catalog/create_version.html', context)


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

