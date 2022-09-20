from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Item

@login_required(login_url='accounts/login/')
def items(request):
    items = Item.objects.all().order_by('name')
    return render(request, 'items.html', {'items': items})


@login_required(login_url='accounts/login/')
def summary(request):
    total_cost = Item.objects.aggregate(Sum('price'))['price__sum']
    return render(request, 'summary.html', {'total_cost': total_cost})


@login_required(login_url='accounts/login/')
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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('items')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
