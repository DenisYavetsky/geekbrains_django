from django.shortcuts import render


def main(request):
    title = {'title': 'Главная'}
    context = {}
    context.update(title)
    return render(request, 'index.html', context=context)


def products(request):
    context = {}
    title = {'title': 'Продукты'}
    products = [{'Name': 'Отличный стул',
                 'img': '../../static/img/slider1.jpg',
                 'price': 2585,
                 'red': 'Горячее предложение',
                 'desc': '<p>Расположитесь комфортно.</p><p>Отличное качество материалов позволит вам это.</p> '
                         '<p>Различные цвета </p>'
                         '<p>высочайшийуровень эргономики и прочность. </p> '
                 },
                {'Name': 'Отличный стул',
                 'img': '../../static/img/slider1.jpg',
                 'price': 2585,
                 'red': 'Горячее предложение',
                 'desc': '<p>Расположитесь комфортно.</p><p>Отличное качество материалов позволит вам это.</p> '
                         '<p>Различные цвета </p>'
                         '<p>высочайшийуровень эргономики и прочность. </p> '
                 },
                {'Name': 'Отличный стул',
                 'img': '../../static/img/slider1.jpg',
                 'price': 2585,
                 'red': 'Горячее предложение',
                 'desc': '<p>Расположитесь комфортно.</p><p>Отличное качество материалов позволит вам это.</p> '
                         '<p>Различные цвета </p>'
                         '<p>высочайшийуровень эргономики и прочность. </p> '
                 }
                ]
    context.update(title)
    context['products'] = products
    return render(request, 'products.html', context=context)


def contact(request):
    title = {'title': 'Контакты'}
    context = {}
    context.update(title)
    return render(request, 'contact.html', context=context)
