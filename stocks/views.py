from django.contrib import messages
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
from anushree.decorators import group_required
from stocks.forms import TyreStockForm, TubeStockForm
from stocks.models import Stock


@group_required('admin', raise_exception=True)
def add_tyre_stock(request):
    context = {}
    form = TyreStockForm(request.POST or None)

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
                    return redirect('stocks:add_tyre_stock')
            except IntegrityError as e:
                print(e)
                messages.error(request, str(e))
                return render()

    context['form'] = form
    return render(request, 'stocks/tyre_create.html', context)


@group_required('admin', raise_exception=True)
def add_tube_stock(request):
    context = {}
    form = TubeStockForm(request.POST or None)

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
                    return redirect('stocks:add_tube_stock')
            except IntegrityError as e:
                print(e)
                messages.error(request, str(e))
                return redirect('stocks:add_tube_stock')

    context['form'] = form
    return render(request, 'stocks/tube_create.html', context)


@group_required('admin', raise_exception=True)
def list_tube_stock(request):
    context = {}

    datas = Stock.objects.filter(item__category__name__icontains="tube")

    context['datas'] = datas
    context['category'] = "Tube"
    return render(request, 'stocks/history_list.html', context)


@group_required('admin', raise_exception=True)
def list_tyre_stock(request):
    context = {}

    datas = Stock.objects.filter(item__category__name__icontains="tyre")

    context['datas'] = datas
    context['category'] = "Tyre"
    return render(request, 'stocks/history_list.html', context)


@group_required('admin', raise_exception=True)
def create_home(request):
    return render(request, 'stocks/create_home.html')


@group_required('admin', raise_exception=True)
def history_home(request):
    return render(request, 'stocks/history_home.html')
