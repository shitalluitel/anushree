import json

from django.db import models

# Create your models here.
from django.dispatch import receiver

from anushree.slugify import unique_slug_generator
from categories.models import Category


# from settings.models import Type, TireDesign, TradePattern, TradeMark


def get_document_filename(instance, filename):
    return "products/%s" % (instance.name + '.' + filename.split('.')[-1])


class ProductQuerySet(models.QuerySet):

    def serialize(self):
        qs = self
        final_array = []
        for obj in qs:
            stuct = json.loads(obj.serialize())
            final_array.append(stuct)
        return json.dumps(final_array)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


class Product(models.Model):
    pattern_name = models.CharField(max_length=64, null=True, blank=True)
    pattern_code = models.CharField(max_length=16, null=True, blank=True)
    size = models.CharField(max_length=32)

    pr = models.CharField(max_length=32, null=True, blank=True)
    product_name = models.CharField(max_length=64, null=True, blank=True)
    stock = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING)
    is_deleted = models.BooleanField(default=False)

    slug = models.SlugField(unique=True, null=True, blank=True)

    timestamp = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.product_name or self.pattern_code

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        unique_together = ('pattern_name', 'pattern_code', 'product_name')

    def serialize(self):
        data = {
            "id": self.id,
            "pattern_name": self.pattern_name,
            "pattern_code": self.pattern_code,
            "size": self.size,
            "pr": self.pr,
            "product_name": self.product_name,
            "stock": self.stock,
            "price": float(self.price),
            "category": str(self.category),
            "is_deleted": self.is_deleted,
            'created_at': str(self.timestamp),
            "error": False,
        }

        data = json.dumps(data)
        return data


@receiver(models.signals.pre_save, sender=Product)
def auto_slug_generator(sender, instance, **kwargs):
    """
    Creates a slug if there is no slug.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, new_slug=instance.product_name or instance.pattern_name)
