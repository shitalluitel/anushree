import json
import os

from io import StringIO, BytesIO

from datetime import datetime

from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from django.db import models

# Create your models here.
from django.dispatch import receiver

from anushree.settings import MEDIA_ROOT
from anushree.slugify import unique_slug_generator


def get_document_filename(instance, filename):
    return "sliderimages/original/%s" % (instance.name + '.' + filename.split('.')[-1])


def get_thumbnail_filename(instance, filename):
    return "sliderimages/thumbnail/%s" % (instance.name + '.' + filename.split('.')[-1])


class UpdateQuerySet(models.QuerySet):

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


class SliderImageManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class SliderImage(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to=get_document_filename, verbose_name='SliderImage', )
    thumbnail = models.ImageField(upload_to=get_thumbnail_filename, editable=False)
    description = models.TextField(max_length=512)

    slug = models.SlugField(unique=True, null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = SliderImageManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'slider_image'
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'

    def serialize(self):
        try:
            image = self.image.name.split('/')[2]
        except Exception as e:
            print(e)
            image = ""

        try:
            thumbnail = self.thumbnail.name.split('/')[2]
        except Exception as e:
            print(e)
            thumbnail = ""

        data = {
            "id": self.id,
            "name": self.name,
            "image": image,
            "thumbnail": thumbnail,
            "slug": self.slug,
            "description": self.description,
            "error": False,
        }

        data = json.dumps(data)
        return data


# @receiver(models.signals.pre_save, sender=SliderImage)
# def auto_delete_image_on_change(sender, instance, **kwargs):
#     """
#     Deletes old image from imagesystem
#     when corresponding `Mediaimage` object is updated
#     with new image.
#     """
#     if not instance.pk:
#         return False
#
#     try:
#         image = SliderImage.objects.get(pk=instance.pk)
#     except SliderImage.DoesNotExist:
#         return False
#     old_image = image.image
#     old_thumbnail = image.thumbnail
#
#     new_image = instance.image
#     new_thumbnail = instance.thumbnail
#
#     print("old : {}, new: {}".format(old_thumbnail, new_thumbnail))
#
#     if not old_image == new_image:
#         if os.path.isfile(old_image.path):
#             os.remove(old_image.path)
#
#     if not old_thumbnail == new_thumbnail:
#         if os.path.isfile(old_thumbnail.path):
#             os.remove(old_thumbnail.path)
#

@receiver(models.signals.pre_save, sender=SliderImage)
def auto_slug_generator(sender, instance, **kwargs):
    """
    Creates a slug if there is no slug.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, new_slug=instance.name)

    image = Image.open(instance.image)

    image.thumbnail([500, 500], Image.ANTIALIAS)

    thumb_extension = os.path.splitext(instance.image.name)[1]
    thumb_extension = thumb_extension.lower()

    thumb_filename = instance.image.name

    if thumb_extension in ['.jpg', '.jpeg']:
        FTYPE = 'JPEG'
    elif thumb_extension == '.gif':
        FTYPE = 'GIF'
    elif thumb_extension == '.png':
        FTYPE = 'PNG'
    else:
        return False  # Unrecognized file type

    # Save thumbnail to in-memory file as StringIO
    temp_thumb = BytesIO()
    image.save(temp_thumb, FTYPE)
    temp_thumb.seek(0)

    # set save=False, otherwise it will run in an infinite loop
    instance.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
    instance.thumbnail = instance.thumbnail
    temp_thumb.close()

    return True


# @receiver(models.signals.post_delete, sender=SliderImage)
# def auto_delete_folder_on_delete(sender, instance, **kwargs):
#     for root, dirs, files in os.walk(MEDIA_ROOT):
#         for d in dirs:
#             dir = os.path.join(root, d)
#             # check if dir is empty
#             if not os.listdir(dir):
#                 os.rmdir(dir)


@receiver(models.signals.pre_delete, sender=SliderImage)
def auto_pre_delete_image_on_delete(sender, instance, **kwargs):
    """
    Deletes image from imagesystem
    when corresponding `Mediaimage` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)


@receiver(models.signals.pre_save, sender=SliderImage)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """
    Deletes old image from imagesystem
    when corresponding `Mediaimage` object is updated
    with new image.
    """
    if not instance.pk:
        return False

    try:
        image = SliderImage.objects.get(pk=instance.pk)
    except SliderImage.DoesNotExist:
        return False

    old_image = image.image
    old_thumbnail = image.thumbnail

    new_image = instance.image
    new_thumbnail = instance.image

    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)

    if not old_thumbnail == new_thumbnail:
        if os.path.isfile(old_thumbnail.path):
            os.remove(old_thumbnail.path)
