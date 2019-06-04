from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from categories.models import Category
from products.forms import TubeForm, TyreForm, TubeEditForm
from products.models import Product


@permission_required('products.add_product', raise_exception=True)
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


@permission_required('products.add_product', raise_exception=True)
def tyre_create(request):
    context = {}
    form = TyreForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                category = Category.objects.get(name__icontains='tyre', is_deleted=False)
            except Category.DoesNotExist as e:
                messages.warning(request, str(e))
                return render(request, 'products/tyre/create.html', context)

            tyre = form.save(commit=False)
            tyre.category = category
            tyre.save()

            messages.success(request, "Successfully created Tyre product.")
            # return redirect('')

    context['form'] = form

    return render(request, 'products/tyre/create.html', context)


@login_required
def tyre_list(request):
    context = {}
    user = request.user
    datas = Product.objects.filter(category__name__icontains="tyre", is_deleted=False)

    category = datas.first().category.is_deleted

    if category:
        messages.warning(request, 'Category for these data has been deleted or inactive.')

    context['datas'] = datas
    try:
        if not user.groups.name == 'admin' and not user.is_superuser:
            product_detail = user.cart.items.all()
            items = ([x.product for x in product_detail])
            context['cart_item'] = items
    except Exception as e:
        print(e)
    return render(request, 'products/tyre/list.html', context)


@login_required
def tube_list(request):
    context = {}
    user = request.user
    datas = Product.objects.filter(category__name__icontains="tube", is_deleted=False)

    category = datas.first().category.is_deleted

    if category:
        messages.warning(request, 'Category for these data has been deleted or inactive.')

    context['datas'] = datas

    if not user.groups.name == 'admin' and not user.is_superuser:
        product_detail = user.cart.items.all()
        items = ([x.product for x in product_detail])
        context['cart_item'] = items

    return render(request, 'products/tube/list.html', context)


@permission_required('products.change_product', raise_exception=True)
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


@permission_required('products.change_product', raise_exception=True)
def tyre_edit(request, slug):
    context = {}

    try:
        data = Product.objects.get(slug=slug, category__name__icontains='tyre')
    except Product.DoesNotExist as e:
        messages.error(request, str(e))
        return redirect('products:tyre_list')

    form = TyreForm(request.POST or None, instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            messages.success(request, "Successfully updated Tyre product.")
            return redirect('products:tyre_list')

    context['form'] = form
    return render(request, 'products/tyre/create.html', context)


@permission_required('products.delete_product', raise_exception=True)
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


@permission_required('products.delete_product', raise_exception=True)
def tyre_delete(request, slug):
    context = {}
    if request.method == "POST":
        try:
            data = Product.objects.get(slug=slug, category__name__icontains='tyre')
            if data.is_deleted:
                data.delete()
                messages.success(request, 'This data has been deleted permanently.')
                return redirect('archive:tube_archive')
            else:
                data.is_deleted = True
                data.save()
                messages.success(request, 'This data has been deleted.')

                return redirect('products:tyre_list')

        except Product.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('products:tyre_list')

    context['next'] = reverse('archive:tyre_archive')
    context['page_name'] = "Product Tyre"
    context['message'] = "Do you want to delete this data? It may be lost permanently."
    context['status'] = 'Delete'

    return render(request, 'snippets/delete.html', context)


@permission_required('products.delete_product', raise_exception=True)
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


@permission_required('products.delete_product', raise_exception=True)
def tyre_undo(request, slug):
    context = {}
    if request.method == "POST":
        try:
            data = Product.objects.get(slug=slug, category__name__icontains='tyre')

            data.is_deleted = False
            data.save()
            messages.success(request, 'This data has been restored.')

            return redirect('archive:tyre_archive')

        except Product.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('archive:tyre_archive')

    context['next'] = reverse('archive:tyre_archive')
    context['page_name'] = "Product Tyre"
    context['message'] = "Do you want to undo this data?"
    context['status'] = 'Undo'

    return render(request, 'snippets/delete.html', context)


@login_required
def product_home(request):
    return render(request, 'products/product_home.html')
