from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from categories.forms import CategoryForm
from categories.models import Category


def create(request):
    context = {}
    form = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created category.')
            return redirect('categories:create')

    context['form'] = form
    return render(request, 'categories/create.html', context)


def list(request):
    context = {}
    datas = Category.objects.all()

    context['datas'] = datas
    return render(request, 'categories/list.html', context)


def edit(request, pk):
    context = {}
    try:
        data = Category.objects.get(pk=pk)
    except Category.DoesNotExist as e:
        messages.error(request, e)
        return redirect('category:list')

    form = CategoryForm(request.POST or None, instance=data)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created category.')
            return redirect('categories:create')

    context['form'] = form
    return render(request, 'categories/create.html', context)


def delete(request, pk):
    context = {}
    if request.method == 'POST':
        try:
            data = Category.objects.get()
            if data.is_deleted:
                data.delete()
            else:
                data.is_deleted = True
                data.save()
        except Category.DoesNotExist as e:
            messages.error(request, e)
            return redirect('categories:list')

        messages.success(request, 'Successfully deleted the category record.')

    context['next'] = reverse('categories:list')
    context['page_name'] = "Category"
    context['status'] = 'Delete'
    return render(request, 'snippets/delete.html', context)


def undo(request, pk):
    context = {}
    if request.method == 'POST':
        try:
            data = Category.objects.get()

            data.is_deleted = False
            data.save()
        except Category.DoesNotExist as e:
            messages.error(request, e)
            return redirect('categories:list')

        messages.success(request, 'Successfully restored the category record.')

    context['next'] = reverse('categories:list')
    context['page_name'] = "Category"
    context['status'] = 'Undo'
    return render(request, 'snippets/delete.html', context)
