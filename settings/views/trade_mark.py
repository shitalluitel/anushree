import json

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from settings.forms import TradeMarkForm, TradeMark


def create(request):
    context = {}
    form = TradeMarkForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            course = form.save()
            messages.success(request, "Successfully created '{}' course".format(course.name))
            return redirect("trade_mark:create")

    context['form'] = form
    return render(request, 'trade_mark/create.html', context)


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
            course = form.save()
            messages.success(request, "Successfully updated '{}' course".format(course.name))
            return redirect("trade_mark:list")

    context['form'] = form
    return render(request, 'trade_mark/create.html', context)


@login_required
def list(request):
    context = {}
    datas = TradeMark.objects.all()
    context['datas'] = datas
    return render(request, 'trade_mark/list.html', context)


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

        messages.success(request, "Successfully deleted {}.".format(data.name))
        return redirect('trade_mark:list')

    context['next'] = reverse('trade_mark:list')
    context['page_name'] = "TradeMarks"
    return render(request, 'snippets/delete.html', context)
