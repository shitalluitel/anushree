from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from notifications.signals import notify

from orders.models import Order, Cart, CartItem, OrderItem
from products.models import Product
from django.db.models import Sum, F, FloatField

from users.models import User


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


@login_required
def cart_home(request):
    context = {}

    user = request.user
    cart_items = user.cart.items.all()
    context['cart_items'] = cart_items
    return render(request, 'orders/cart_display.html', context)


@login_required
def add_to_cart(request):
    cart, cart_new = Cart.objects.get_or_create(customer=request.user)
    print(request.POST)
    try:
        product = Product.objects.get(
            pk=request.POST['product_id']
        )
        quantity = int(request.POST['quantity'])
    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')

    # Disallow adding to cart if available inventory is not enough
    if quantity > product.stock:
        messages.error(request, 'Product Out of Stock.')
        return redirect('home')

    existing_cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if existing_cart_item:
        existing_cart_item.quantity = quantity
        existing_cart_item.save()
    else:
        new_cart_item = CartItem(cart=cart, product=product, quantity=quantity)
        new_cart_item.save()

    # serializer = CartSerializer(cart)
    messages.success(request, 'Product added to cart.')

    return redirect('orders:cart_home')


@login_required
def remove_from_cart(request):
    cart, cart_new = Cart.objects.get_or_create(customer=request.user)

    try:
        product = Product.objects.get(
            pk=request.POST['product_id']
        )
    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')

    cart_item.delete()

    messages.success(request, 'Product removed from cart.')

    return redirect('orders:cart_home')


@login_required
def destroy_cart(request):
    user = request.user

    cart_items = user.cart.items.all()

    if cart_items.count() == 0:
        messages.warning(request, "There is no any items in cart to destroy.")
        return redirect('orders:cart_home')

    for item in cart_items:
        item.delete()

    messages.success(request, "Successfully destroyed cart.")
    return redirect('orders:cart_home')


@login_required
@transaction.atomic
def order_create(request):
    user = request.user

    cart_items = user.cart.items.all()

    for cart_item in cart_items:
        if cart_item.product.stock - cart_item.quantity < 0:
            messages.error(request, 'We do not have enough stock of ' + str(cart_item.product) + \
                           'to complete your purchase. Sorry, we will restock soon')
            return redirect('orders:cart_home')

    if cart_items.count() == 0:
        messages.error(request, 'Your Cart is empty')
        return redirect('orders:cart_home')

    try:
        total_aggregated_dict = cart_items.aggregate(
            total=Sum(F('quantity') * F('product__price'), output_field=FloatField()))

        order_total = round(total_aggregated_dict['total'], 2)
        order = Order(customer=user, total=order_total)
        order.save()

        print(order)
    except Exception as e:
        print(e)
        messages.error(request, str(e))
        return redirect('orders:cart_home')

    order_items = []
    try:
        for cart_item in cart_items:
            order_items.append(OrderItem(order=order, product=cart_item.product, quantity=cart_item.quantity))

            # available_inventory should decrement by the appropriate amount
            cart_item.product.stock -= cart_item.quantity
            cart_item.product.save()

            cart_item.delete()

            # order_item.save()

        OrderItem.objects.bulk_create(order_items)

        # group = Group.objects.get(name__icontains='admin')
        admin = User.objects.filter(is_superuser=True)
        notify.send(sender=request.user, recipient=admin,
                    verb='Order for Items by {}'.format(user.get_full_name()),
                    description="{} ordered for {} items.".format(user.get_full_name(),
                                                                  user.cart.items.all().count()))

    except Exception as e:
        print(e)
        messages.error(request, str(e))

    return redirect('orders:cart_home')


@login_required
def order_history(request):
    context = {}
    data = Order.objects.filter(customer=request.user, status__iexact='confirmed')
    print(data)
    context['orders'] = data
    return render(request, 'orders/order_history.html', context)


@login_required
def order_history_detail(request, pk):
    context = {}
    order_item = OrderItem.objects.filter(order__id=pk)
    context['cart_items'] = order_item
    return render(request, 'orders/order_history_detail.html', context)


@login_required
def order_detail(request, pk):
    context = {}
    order_item = OrderItem.objects.filter(order__id=pk)
    context['cart_items'] = order_item
    return render(request, 'orders/order_detail.html', context)

#
# @login_required
# def order_list(request):
#     context = {}
#     orders = Order.objects.filter(status__iexact='new')
#     context['orders'] = orders
#
#     return render(request, 'orders/')
