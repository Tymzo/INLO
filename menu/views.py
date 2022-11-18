from django.shortcuts import render

from django.http import HttpResponse
import datetime

from menu.models import Pizza


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}, </body> </html>"
    return HttpResponse(html)


def pizzas(request):
    context = {'pizzas': Pizza.objects.all()}
    return render(request, 'menu.html', context)


def create_pizza(request):
    return render(request,'create_pizza.html')
