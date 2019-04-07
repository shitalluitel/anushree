from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from products.models import Product
from users.models import User


class Stock(models.Model):
    item = models.ForeignKey(Product, related_name='stocks', on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(validators=[
        MinValueValidator(1)
    ])
    user = models.ForeignKey(User, related_name='stocks', on_delete=models.DO_NOTHING)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        db_table = 'stocks'
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
