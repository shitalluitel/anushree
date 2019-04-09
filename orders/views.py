from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from notifications.signals import notify

from orders.models import Order


@permission_required('orders.add_order')
def new_order_list(request):
    context = {}
    orders = Order.objects.filter(status='new')
    context['orders'] = orders
    return render(request, 'orders/new_order_list.html', context)


@permission_required('orders.add_order')
def confirm_order(request, pk):
    order = None

    try:
        order = Order.objects.get(pk=pk)
    except Exception as e:
        print(e)
        messages.error(request, str(e))

    user = order.customer

    order.status = 'confirmed'
    order.save()

    notify.send(sender=request.user, recipient=user,
                verb='Book order by ' + request.user.get_full_name(),
                description="Your Order for product {} has been {}".format(order.id, order.status))

    messages.success(request, 'Order {} has been confirmed.'.format(order.id))
    return redirect('orders:new_order_list')


@permission_required('orders.add_order')
def reject_order(request, pk):
    order = None

    try:
        order = Order.objects.get(pk=pk)
    except Exception as e:
        print(e)
        messages.error(request, str(e))

    user = order.customer

    notify.send(sender=request.user, recipient=user,
                verb='Book order by ' + request.user.get_full_name(),
                description="".format())

    order.status = 'rejected'
    order.save()

    notify.send(sender=request.user, recipient=user,
                verb='Book order by ' + request.user.get_full_name(),
                description="Your Order for product {} has been {}".format(order.id, order.status))

    messages.warning(request, 'Order {} has been rejected.'.format(order.id))
    return redirect('orders:new_order_list')
