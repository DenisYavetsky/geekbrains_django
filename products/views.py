from django.shortcuts import render
from products.models import Product, ProductCategory


def main(request):
    title = {'title': 'Главная'}
    context = {}
    context.update(title)
    return render(request, 'index.html', context=context)


def products(request):
    context = {}
    title = {'title': 'Продукты'}
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context.update(title)
    context['products'] = products
    context['category'] = categories
    return render(request, 'products.html', context=context)


def contact(request):
    title = {'title': 'Контакты'}
    context = {}
    context.update(title)
    return render(request, 'contact.html', context=context)
