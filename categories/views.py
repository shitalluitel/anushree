from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from categories.forms import CategoryForm
from categories.models import Category

@login_required
@permission_required('categories.add_category', raise_exception=True)
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

@login_required
def list(request):
    context = {}
    datas = Category.objects.filter(is_deleted=False)

    context['datas'] = datas
    return render(request, 'categories/list.html', context)

@login_required
@permission_required('categories.change_category', raise_exception=True)
def edit(request, slug):
    context = {}
    try:
        data = Category.objects.get(slug=slug)
    except Category.DoesNotExist as e:
        messages.error(request, str(e))
        return redirect('categories:list')

    form = CategoryForm(request.POST or None, instance=data)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created category.')
            return redirect('categories:create')

    context['form'] = form
    return render(request, 'categories/create.html', context)

@login_required
@permission_required('categories.delete_category')
def delete(request, slug):
    context = {}
    if request.method == 'POST':
        try:
            data = Category.objects.get(slug=slug)
            if data.is_deleted:
                products_count = data.products.count()
                if products_count > 0:
                    messages.error(request,
                                   "Unable to delete record. There are some product related with this category.")
                    return redirect('archive:category_archive')

                data.delete()

                messages.success(request, 'Permanently deleted category data.')
                return redirect('archive:category_list')
            else:
                data.is_deleted = True
                data.save()

                messages.success(request, 'Successfully deleted category record.')
                return redirect('categories:list')
        except Category.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('categories:list')

    context['next'] = reverse('categories:list')
    context['page_name'] = "Category"
    context['status'] = 'Delete'
    context['message'] = "Do you want to delete this data? It may be lost permanently."

    return render(request, 'snippets/delete.html', context)

@login_required
@permission_required('categories.delete_category')
def undo(request, slug):
    context = {}
    if request.method == 'POST':
        try:
            data = Category.objects.get(slug=slug)

            data.is_deleted = False
            data.save()

            messages.success(request, 'Successfully restored category data.')
            return redirect('archive:category_archive')
        except Category.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('archive:category_archive')

    context['next'] = reverse('archive:category_archive')
    context['page_name'] = "Category"
    context['status'] = 'Undo'
    context['message'] = "Do you want to undo this data?"

    return render(request, 'snippets/delete.html', context)
