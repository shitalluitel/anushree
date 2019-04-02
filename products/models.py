import json

from django.db import models

# Create your models here.


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
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.FileField(upload_to=get_document_filename, verbose_name='SliderImage', )
    description = models.TextField(max_length=252, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING)

    timestamp = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def serialize(self):
        try:
            image = self.image.name.split('/')[1]
        except:
            image = ""

        data = {
            "id": self.id,
            "name": self.name,
            "image": image,
            "description": self.description,
            "price": float(self.price),
            "error": False,
        }

        data = json.dumps(data)
        return data
