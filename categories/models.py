import json

from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.utils.text import slugify


class CategoryQuerySet(models.QuerySet):

    # def serialize(self):
    #     list_values = list(self.values('id', 'name', 'image', 'description'))
    #     return json.dumps(list_values)

    def serialize(self):
        qs = self
        final_array = []
        for obj in qs:
            stuct = json.loads(obj.serialize())
            final_array.append(stuct)
        return json.dumps(final_array)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)


class Category(models.Model):
    name = models.CharField(max_length=64)
    slugs = models.CharField(max_length=64, blank=True)

    timestamp = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def serialize(self):
        data = {
            "id": self.id,
            "name": self.name,
            "error": False,
        }

        data = json.dumps(data)
        return data


@receiver(models.signals.pre_save, sender=Category)
def slugify_name(sender, instance, **kwargs):
    """
    Deletes document from documentsystem
    when corresponding `Mediadocument` object is deleted.
    """
    instance.slugs = slugify(instance.name)
