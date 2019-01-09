from django.shortcuts import render
from .models import Menu

# Create your views here.

def home_page(request):
    menus = Menu.objects.filter()
    stuff_for_frontend = {'menus': menus}
    return render(request, 'menu/home_page.html', stuff_for_frontend)