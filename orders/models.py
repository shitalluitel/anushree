import json

from django.db import models
# from model_utils import Choices

from anushree import settings

# Create your models here.
from products.models import Product


# STATUS = Choices('new', 'confirmed', 'rejected')


class Cart(models.Model):
    """A model that contains data for a shopping cart."""
    customer = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def serialize(self):
        cart_items = self.items.all()
        data = {
            "id": self.id,
            "order_item": list(
                [{'product': json.loads(x.product.serialize()), 'quantity': x.quantity} for x in cart_items]),
            "created_at": str(self.created_at.date()),
            "error": False,
        }

        # data = json.dumps(data)
        return data


class CartItem(models.Model):
    """A model that contains data for an item in the shopping cart."""
    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        related_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return '%s: %s' % (self.product.product_name or self.product.pattern_code, self.quantity)

    @staticmethod
    def get_items_count(request):
        user = request.user
        if user.is_authenticated and not user.is_superuser and not user.groups.name == 'admin':
            count = user.cart.items.all().count()
            return count
        return None


class OrderQuerySet(models.QuerySet):

    def serialize(self):
        qs = self
        final_array = []
        for obj in qs:
            stuct = json.loads(obj.serialize())
            final_array.append(stuct)
        return json.dumps(final_array)


class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)


class Order(models.Model):
    """
    An Order is the more permanent counterpart of the shopping cart. It represents
    the frozen the state of the cart on the moment of a purchase. In other words,
    an order is a customer purchase.
    """
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='orders',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=16, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = OrderManager()

    def __str__(self):
        return str(self.id)

    def serialize(self):
        order_items = self.order_items.all()
        data = {
            "id": self.id,
            "total": float(self.total),
            "order_item": list(
                [{'product': json.loads(x.product.serialize()), 'quantity': x.quantity} for x in order_items]),
            "created_at": str(self.created_at.date()),
            "status": self.status,
            "error": False,
        }

        data = json.dumps(data)
        return data


class OrderItem(models.Model):
    """A model that contains data for an item in an order."""
    order = models.ForeignKey(
        Order,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return '%s: %s' % (self.product.product_name or self.product.pattern_code, self.quantity)
