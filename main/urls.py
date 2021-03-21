from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('authorization', views.authorization, name='authorization'),
    path('account', views.account, name='account'),
    path('calendar', views.calendar, name='calendar')
]