from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from categories.models import Category
from products.forms import TubeForm, TireForm, TubeEditForm
from products.models import Product


def tube_create(request):
    context = {}
    form = TubeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                category = Category.objects.get(name__icontains='tube', is_deleted=False)
            except Category.DoesNotExist as e:
                messages.warning(request, str(e))
                return render(request, 'products/tube/create.html', context)
            tube = form.save(commit=False)
            tube.category = category
            tube.save()

            messages.success(request, "Successfully created Tube product.")
            return redirect('products:tube_create')
        print(form.errors)
    context['form'] = form
    return render(request, 'products/tube/create.html', context)


def tire_create(request):
    context = {}
    form = TireForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                category = Category.objects.get(name__icontains='tire', is_deleted=False)
            except Category.DoesNotExist as e:
                messages.warning(request, str(e))
                return render(request, 'products/tire/create.html', context)

            tire = form.save(commit=False)
            tire.category = category
            tire.save()

            messages.success(request, "Successfully created Tire product.")
            # return redirect('')

    context['form'] = form

    return render(request, 'products/tire/create.html', context)


def tire_list(request):
    context = {}
    datas = Product.objects.filter(category__name__icontains="tire", is_deleted=False)

    category = datas.first().category.is_deleted

    if category:
        messages.warning(request, 'Category for these data has been deleted or inactive.')

    context['datas'] = datas
    if not request.user.groups == 'admin':
        product_detail = request.user.cart.items.all()
        items = ([x.product for x in product_detail])
        context['cart_item'] = items
    return render(request, 'products/tire/list.html', context)


def tube_list(request):
    context = {}
    datas = Product.objects.filter(category__name__icontains="tube", is_deleted=False)

    category = datas.first().category.is_deleted

    if category:
        messages.warning(request, 'Category for these data has been deleted or inactive.')

    context['datas'] = datas

    if not request.user.groups == 'admin':
        product_detail = request.user.cart.items.all()
        items = ([x.product for x in product_detail])
        context['cart_item'] = items

    return render(request, 'products/tube/list.html', context)


def tube_edit(request, slug):
    context = {}
    try:
        data = Product.objects.get(slug=slug, category__name__icontains='tube')
    except Product.DoesNotExist as e:
        messages.error(request, str(e))
        return redirect('products:tube_list')

    form = TubeEditForm(request.POST or None, instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            messages.success(request, "Successfully updated Tube product.")
            return redirect('products:tube_list')

    context['form'] = form
    return render(request, 'products/tube/create.html', context)


def tire_edit(request, slug):
    context = {}

    try:
        data = Product.objects.get(slug=slug, category__name__icontains='tire')
    except Product.DoesNotExist as e:
        messages.error(request, str(e))
        return redirect('products:tire_list')

    form = TireForm(request.POST or None, instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            messages.success(request, "Successfully updated Tire product.")
            return redirect('products:tire_list')

    context['form'] = form
    return render(request, 'products/tire/create.html', context)


def tube_delete(request, slug):
    context = {}
    if request.method == "POST":
        try:
            data = Product.objects.get(slug=slug, category__name__icontains='tube')
            if data.is_deleted:
                data.delete()
                messages.success(request, 'This data has been deleted permanently.')
                return redirect('archive:tube_archive')
            else:
                data.is_deleted = True
                data.save()
                messages.success(request, 'This data has been deleted.')
                return redirect('products:tube_list')

        except Product.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('products:tube_list')

    context['next'] = reverse('products:tube_list')
    context['page_name'] = "Product Tube"
    context['message'] = "Do you want to delete this data? It may be lost permanently."
    context['status'] = 'Delete'

    return render(request, 'snippets/delete.html', context)


def tire_delete(request, slug):
    context = {}
    if request.method == "POST":
        try:
            data = Product.objects.get(slug=slug, category__name__icontains='tire')
            if data.is_deleted:
                data.delete()
                messages.success(request, 'This data has been deleted permanently.')
                return redirect('archive:tube_archive')
            else:
                data.is_deleted = True
                data.save()
                messages.success(request, 'This data has been deleted.')

                return redirect('products:tire_list')

        except Product.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('products:tire_list')

    context['next'] = reverse('archive:tire_archive')
    context['page_name'] = "Product Tire"
    context['message'] = "Do you want to delete this data? It may be lost permanently."
    context['status'] = 'Delete'

    return render(request, 'snippets/delete.html', context)


def tube_undo(request, slug):
    context = {}
    if request.method == "POST":
        try:
            data = Product.objects.get(slug=slug, category__name__icontains='tube')

            data.is_deleted = False
            data.save()
            messages.success(request, 'This data has been restored.')

            return redirect('archive:tube_archive')

        except Product.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('archive:tube_archive')

    context['next'] = reverse('archive:tube_archive')
    context['page_name'] = "Product Tube"
    context['message'] = "Do you want to undo this data?"
    context['status'] = 'Undo'

    return render(request, 'snippets/delete.html', context)


def tire_undo(request, slug):
    context = {}
    if request.method == "POST":
        try:
            data = Product.objects.get(slug=slug, category__name__icontains='tire')

            data.is_deleted = False
            data.save()
            messages.success(request, 'This data has been restored.')

            return redirect('archive:tire_archive')

        except Product.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('archive:tire_archive')

    context['next'] = reverse('archive:tire_archive')
    context['page_name'] = "Product Tire"
    context['message'] = "Do you want to undo this data?"
    context['status'] = 'Undo'

    return render(request, 'snippets/delete.html', context)
