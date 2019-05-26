import json

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from anushree.decorators import group_required
from categories.models import Category
from products.models import Product


@group_required('admin', raise_exception=True)
def archive_home(request):
    return render(request, 'archive/home.html')


@group_required('admin', raise_exception=True)
def product_archive_home(request):
    return render(request, 'archive/product_archive_home.html')


@group_required('admin', raise_exception=True)
def tube_archive(request):
    context = {}
    datas = Product.objects.filter(is_deleted=True, category__name__icontains='tube')

    context['datas'] = datas
    return render(request, 'archive/tube_list.html', context)


@group_required('admin', raise_exception=True)
def tire_archive(request):
    context = {}
    datas = Product.objects.filter(is_deleted=True, category__name__icontains='tire')

    context['datas'] = datas
    return render(request, 'archive/tire_list.html', context)


@group_required('admin', raise_exception=True)
def category_archive(request):
    context = {}
    datas = Category.objects.filter(is_deleted=True)

    context['datas'] = datas
    context['archived'] = True
    return render(request, 'archive/category_list.html', context)
