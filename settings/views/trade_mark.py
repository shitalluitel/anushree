import json

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from anushree.decorators import group_required
from settings.forms import TradeMarkForm, TradeMark


@group_required('admin', raise_exception=True)
def create(request):
    context = {}
    form = TradeMarkForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            data = form.save()
            messages.success(request, "Successfully created '{}' data".format(data))
            return redirect("trade_mark:create")

    context['form'] = form
    return render(request, 'trade_mark/create.html', context)


@group_required('admin', raise_exception=True)
def edit(request, pk):
    context = {}
    try:
        data = TradeMark.objects.get(id=pk)
    except TradeMark.DoesNotExist:
        messages.warning(request, 'Unable to find data that you have requested.')
        return redirect("trade_mark:list")

    form = TradeMarkForm(request.POST or None, instance=data)

    if request.method == "POST":
        if form.is_valid():
            data = form.save()
            messages.success(request, "Successfully updated '{}' data".format(data))
            return redirect("trade_mark:list")

    context['form'] = form
    return render(request, 'trade_mark/create.html', context)


@group_required('admin', raise_exception=True)
def list(request):
    context = {}
    datas = TradeMark.objects.all()
    context['datas'] = datas
    return render(request, 'trade_mark/list.html', context)


@group_required('admin', raise_exception=True)
def delete(request, pk):
    context = {}
    if request.method == "POST":
        try:
            data = TradeMark.objects.get(pk=pk)
            data.delete()
            # data.is_deleted = False
            # data.save()
        except TradeMark.DoesNotExist:
            messages.error(request, "Unable to find data that you have requested.")
            return redirect('trade_mark:list')

        messages.success(request, "Successfully deleted {}.".format(data))
        return redirect('trade_mark:list')

    context['next'] = reverse('trade_mark:list')
    context['page_name'] = "TradeMarks"
    return render(request, 'snippets/delete.html', context)
