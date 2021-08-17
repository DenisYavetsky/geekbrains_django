from django.shortcuts import render


def main(request):
    title = {'title': 'Главная'}
    context = {}
    context.update(title)
    return render(request, 'products/index.html', context=context)


def products(request):
    title = {'title': 'Продукты'}
    context = {}
    context.update(title)
    return render(request, 'products/products.html', context=context)


def contact(request):
    title = {'title': 'Контакты'}
    context = {}
    context.update(title)
    return render(request, 'products/contact.html', context=context)
