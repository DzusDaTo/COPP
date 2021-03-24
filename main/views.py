from django.shortcuts import render
from .models import Articles


def home(request):
     return render(request, 'main/home.html')


def register(request):
     return render(request, 'main/register.html')


def authorization(request):
     return render(request, 'main/authorization.html')


def account(request):
     return render(request, 'main/account.html')


def calendar(request):
     main = Articles.objects.order_by('date')
     return render(request, 'main/calendar.html', {'main': main})