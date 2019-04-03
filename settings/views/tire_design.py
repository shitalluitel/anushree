import json

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from settings.forms import TireDesignForm, TireDesign


def create(request):
    context = {}
    form = TireDesignForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            type = form.save()
            messages.success(request, "Successfully created '{}' type".format(type))
            return redirect("tire_design:create")

    context['form'] = form
    return render(request, 'tire_design/create.html', context)


def edit(request, pk):
    context = {}
    try:
        data = TireDesign.objects.get(id=pk)
    except TireDesign.DoesNotExist:
        messages.warning(request, 'Unable to find data that you have requested.')
        return redirect("tire_design:list")

    form = TireDesignForm(request.POST or None, instance=data)

    if request.method == "POST":
        if form.is_valid():
            type = form.save()
            messages.success(request, "Successfully updated '{}' type".format(type))
            return redirect("tire_design:list")

    context['form'] = form
    return render(request, 'tire_design/create.html', context)


@login_required
def list(request):
    context = {}
    datas = TireDesign.objects.all()
    context['datas'] = datas
    return render(request, 'tire_design/list.html', context)


def delete(request, pk):
    context = {}
    if request.method == "POST":
        try:
            data = TireDesign.objects.get(pk=pk)
            data.delete()
            # data.is_deleted = False
            # data.save()
        except TireDesign.DoesNotExist:
            messages.error(request, "Unable to find data that you have requested.")
            return redirect('tire_design:list')

        messages.success(request, "Successfully deleted {}.".format(data))
        return redirect('tire_design:list')

    context['next'] = reverse('tire_design`:list')
    context['page_name'] = "TireDesigns"
    return render(request, 'snippets/delete.html', context)
