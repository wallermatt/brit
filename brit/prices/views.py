from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Sum

from .models import Item

# Create your views here.
def items(request):
    items = Item.objects.all().order_by('name')
    return render(request, 'items.html', {'items': items})


def summary(request):
    total_cost = Item.objects.aggregate(Sum('price'))['price__sum']
    return render(request, 'summary.html', {'total_cost': total_cost})


def new_item(request):
    if request.method == 'POST':
        item_name = request.POST['name']
        item_price = request.POST['price']
        if not item_name or not item_price:
            return render(request, 'new_item.html', {
                'error_message': "You must enter item name and price",
            })

        new_item = Item(name=item_name, price=item_price)
        new_item.save()
        return HttpResponseRedirect('items')
    return render(request, 'new_item.html') 
