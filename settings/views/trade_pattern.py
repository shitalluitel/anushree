import json

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from settings.forms import TradePatternForm, TradePattern


def create(request):
    context = {}
    form = TradePatternForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            course = form.save()
            messages.success(request, "Successfully created '{}' course".format(course.name))
            return redirect("trade_pattern:create")

    context['form'] = form
    return render(request, 'trade_pattern/create.html', context)


def edit(request, pk):
    context = {}
    try:
        data = TradePattern.objects.get(id=pk)
    except TradePattern.DoesNotExist:
        messages.warning(request, 'Unable to find data that you have requested.')
        return redirect("trade_pattern:list")

    form = TradePatternForm(request.POST or None, instance=data)

    if request.method == "POST":
        if form.is_valid():
            course = form.save()
            messages.success(request, "Successfully updated '{}' course".format(course.name))
            return redirect("trade_pattern:list")

    context['form'] = form
    return render(request, 'trade_pattern/create.html', context)


@login_required
def list(request):
    context = {}
    datas = TradePattern.objects.all()
    context['datas'] = datas
    return render(request, 'trade_pattern/list.html', context)


def delete(request, pk):
    context = {}
    if request.method == "POST":
        try:
            data = TradePattern.objects.get(pk=pk)
            data.delete()
            # data.is_deleted = False
            # data.save()
        except TradePattern.DoesNotExist:
            messages.error(request, "Unable to find data that you have requested.")
            return redirect('trade_pattern:list')

        messages.success(request, "Successfully deleted {}.".format(data.name))
        return redirect('trade_pattern:list')

    context['next'] = reverse('trade_pattern`:list')
    context['page_name'] = "TradePatterns"
    return render(request, 'snippets/delete.html', context)
