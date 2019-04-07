from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
from stocks.forms import TireStockForm


def add_tire_stock(request):
    context = {}
    form = TireStockForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                with transaction.atomic():
                    stock = form.save(commit=False)

                    stock.user = request.user
                    stock.save()

                    item = stock.item

                    item.stock += stock.quantity
                    item.save()
                    return redirect('add_tire_stock')
            except IntegrityError as e:
                print(e)
                return render()

    context['form'] = form
    return render(request, 'stocks/tire_create.html', context)


def add_tube_stock(request):
    context = {}
    form = TireStockForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                with transaction.atomic:
                    stock = form.save(commit=False)

                    stock.user = request.user
                    stock.save()

                    item = stock.item

                    item.stock += stock.quantity
                    item.save()
            except IntegrityError as e:
                print(e)
                return render()

    context['form'] = form
    return render(request, 'stocks/create.html', context)
