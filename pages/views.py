from datetime import datetime
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

from django.db.models import Sum


@login_required
def home_page(request):
    try:
        group = request.user.groups.get()
        group_name = group.name
    except:
        group_name = 'admin'

    if group_name.lower() == 'customer':
        return customer_dashboard(request=request)
    elif group_name.lower() == 'staff' or group_name.lower() == 'admin':
        return admin_dashboard(request=request)


@login_required
def customer_dashboard(request):
    user = request.user
    context = {}

    return render(request, 'pages/_customer_dashboard.html', )


@login_required
def admin_dashboard(request):
    user = request.user
    context = {}

    return render(request, 'pages/_admin_dashboard.html', context)


@login_required
def notification_list(request):
    context = {}
    user = request.user
    notifications = user.notifications.all()

    context['notifications'] = notifications

    return render(request, 'pages/notification_list.html', context)


# @login_required
# def mark_all_as_read(request):
#     context = {}
#     user = request.user
#     notifications = user.notifications.all()
#
#     notifications.mark_all_as_read()
#
#     return redirect('notification_list')
