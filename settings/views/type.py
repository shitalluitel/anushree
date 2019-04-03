import json

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from settings.forms import TypeForm, Type


def create(request):
    context = {}
    form = TypeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            course = form.save()
            messages.success(request, "Successfully created '{}' course".format(course.name))
            return redirect("type:create")

    context['form'] = form
    return render(request, 'type/create.html', context)


def edit(request, pk):
    context = {}
    try:
        data = Type.objects.get(id=pk)
    except Type.DoesNotExist:
        messages.warning(request, 'Unable to find data that you have requested.')
        return redirect("type:list")

    form = TypeForm(request.POST or None, instance=data)

    if request.method == "POST":
        if form.is_valid():
            course = form.save()
            messages.success(request, "Successfully updated '{}' course".format(course.name))
            return redirect("type:list")

    context['form'] = form
    return render(request, 'type/create.html', context)


@login_required
def list(request):
    context = {}
    datas = Type.objects.all()
    context['datas'] = datas
    return render(request, 'type/list.html', context)


def delete(request, pk):
    context = {}
    if request.method == "POST":
        try:
            data = Type.objects.get(pk=pk)
            data.delete()
            # data.is_deleted = False
            # data.save()
        except Type.DoesNotExist:
            messages.error(request, "Unable to find data that you have requested.")
            return redirect('type:list')

        messages.success(request, "Successfully deleted {}.".format(data.name))
        return redirect('type:list')

    context['next'] = reverse('type`:list')
    context['page_name'] = "Types"
    return render(request, 'snippets/delete.html', context)
