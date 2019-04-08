import json

from django.db.models import Sum, F, FloatField
# from django.views.generic.base import View
from rest_framework import viewsets, serializers, status
from rest_framework.decorators import list_route, action
from rest_framework.response import Response

from anushree import settings
# from anushree.mixins import HttpResponseMixin
from orders.api.serializers import CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer
from orders.models import Cart, CartItem, Order, OrderItem
from products.models import Product

User = settings.AUTH_USER_MODEL


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows carts to be viewed or edited.
    """
    permission_classes = []
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(methods=['post', 'put'], detail=False)
    def add_to_cart(self, request, pk=None):
        cart, cart_new = Cart.objects.get_or_create(customer=request.user)

        try:
            product = Product.objects.get(
                pk=request.data['product_id']
            )
            quantity = int(request.data['quantity'])
            print(request.data)
        except Exception as e:
            print(e)
            return Response({'error': str(e)})

        # Disallow adding to cart if available inventory is not enough
        if quantity > product.stock:
            return Response({'error': 'Product Out of Stock.'})

        existing_cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if existing_cart_item:
            existing_cart_item.quantity = quantity
            existing_cart_item.save()
        else:
            new_cart_item = CartItem(cart=cart, product=product, quantity=quantity)
            new_cart_item.save()

        # serializer = CartSerializer(cart)
        return Response(cart.serialize())

    @action(methods=['post', 'put'], detail=False)
    def remove_from_cart(self, request, pk=None):

        cart, cart_new = Cart.objects.get_or_create(customer=request.user)
        print(cart)

        try:
            product = Product.objects.get(
                pk=request.data['product_id']
            )
        except Exception as e:
            return Response({'error': e})

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
        except Exception as e:
            return Response({'error': e})

        cart_item.delete()

        return Response({'error': False})


class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cart items to be viewed or edited.
    """
    permission_classes = []
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or created.
    """
    permission_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = self.request.user

        cart = user.cart

        for cart_item in cart.items.all():
            if cart_item.product.stock - cart_item.quantity < 0:
                raise serializers.ValidationError(
                    'We do not have enough stock of ' + str(cart_item.product) + \
                    'to complete your purchase. Sorry, we will restock soon'
                )

        if cart.items.count() == 0:
            return Response({'error': True, 'detail': 'Your Cart is empty'})

        try:
            total_aggregated_dict = cart.items.aggregate(
                total=Sum(F('quantity') * F('product__price'), output_field=FloatField()))

            order_total = round(total_aggregated_dict['total'], 2)
            order = serializer.save(customer=user, total=order_total)
        except Exception as e:
            print(e)
            return Response({'error': e})

        order_items = []
        try:
            for cart_item in cart.items.all():
                order_items.append(OrderItem(order=order, product=cart_item.product, quantity=cart_item.quantity))
                # available_inventory should decrement by the appropriate amount
                cart_item.product.stock -= cart_item.quantity
                cart_item.product.save()

                cart_item.delete()

            OrderItem.objects.bulk_create(order_items)
        except Exception as e:
            print(e)
            return Response({'error': e})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        try:
            headers = self.get_success_headers(serializer.data)
            return Response({'error': False}, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({'error': True}, status=status.HTTP_400_BAD_REQUEST)

    @list_route(url_path="history")
    def order_history(self, request):
        user = request.user
        orders = Order.objects.filter(customer=user).serialize()
        # serializer = OrderSerializer(orders, many=True)
        serializers = json.loads(orders)
        return Response(serializers)


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order items to be viewed or edited.
    """
    permission_classes = []
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
