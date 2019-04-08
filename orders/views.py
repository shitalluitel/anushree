from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from orders.models import Order


@permission_required('orders.add_order')
def new_order_list(request):
    context = {}
    orders = Order.objects.filter(status='new')
    context['orders'] = orders
    return render(request, 'orders/new_order_list.html', context)


@permission_required('orders.add_order')
def confirm_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Exception as e:
        print(e)
        messages.error(request, e)

    user = order.customer
    try:
        subject = 'Order Confirmed'
        message = 'Your Order created at {} has been confirmed.'.format(order.created_at)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        messages.error(request, e)
        return redirect('orders:new_order_list')

    order.status = 'confirmed'
    order.save()

    messages.success(request, 'Order {} has been confirmed.'.format(order.id))
    return redirect('orders:new_order_list')


@permission_required('orders.add_order')
def reject_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Exception as e:
        print(e)
        messages.error(request, e)

    user = order.customer

    try:
        subject = 'Order Rejected'
        message = 'Your Order created at {} has been rejected.'.format(order.created_at)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        messages.error(request, e)
        return redirect('orders:new_order_list')

    order.status = 'rejected'
    order.save()

    messages.warning(request, 'Order {} has been rejected.'.format(order.id))
    return redirect('orders:new_order_list')
