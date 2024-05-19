from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['']
    }
    return render(request, 'main/homePage.html', data)


def chatgpt(request):
    return render(request, 'main/chatgpt.html')


def telegram(request):
    return render(request, 'main/telegram.html')