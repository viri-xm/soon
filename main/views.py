from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'main/login.html')

