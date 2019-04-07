import json

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from categories.models import Category
from products.models import Product


def archive_home(request):
    return render(request, 'archive/home.html')


def product_archive_home(request):
    return render(request, 'archive/product_archive_home.html')


def tube_archive(request):
    context = {}
    datas = Product.objects.filter(is_deleted=True, category__name__icontains='tube')

    context['datas'] = datas
    return render(request, 'archive/tube_list.html', context)


def tire_archive(request):
    context = {}
    datas = Product.objects.filter(is_deleted=True, category__name__icontains='tire')

    context['datas'] = datas
    return render(request, 'archive/tire_list.html', context)


def category_archive(request):
    context = {}
    datas = Category.objects.filter(is_deleted=True)

    context['datas'] = datas
    return render(request, 'archive/category_list.html', context)
