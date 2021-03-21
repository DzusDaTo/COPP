from django.shortcuts import render


def home(request):
     return render(request, 'main/home.html')


def register(request):
     return render(request, 'main/register.html')


def authorization(request):
     return render(request, 'main/authorization.html')


def account(request):
     return render(request, 'main/account.html')


def calendar(request):
     return render(request, 'main/calendar.html')