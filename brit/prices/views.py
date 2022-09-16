from django.shortcuts import render
from django.db.models import Sum

from .models import Item

# Create your views here.
def items(request):
    items = Item.objects.all()
    return render(request, 'items.html', {'items': items})


def summary(request):
    total_cost = Item.objects.aggregate(Sum('price'))['price__sum']
    return render(request, 'summary.html', {'total_cost': total_cost})


def new_item
