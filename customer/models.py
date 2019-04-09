from django.contrib.auth.models import Group
from django.db import models

# Create your models here.
from django.dispatch import receiver

from users.models import User


# from anushree import settings
#
# User = settings.AUTH_USER_MODEL


class Customer(models.Model):
    owner = models.CharField(max_length=64)
    company = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    mobile_no = models.CharField(max_length=15)
    phone_no = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    pan_no = models.CharField(max_length=16)

    user = models.OneToOneField(User, related_name='customer', on_delete=models.DO_NOTHING)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.company

    class Meta:
        db_table = "customer"
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


@receiver(models.signals.pre_save, sender=Customer)
def add_customer_to_group(sender, instance, **kwargs):
    """
    Creates a slug if there is no slug.
    """
    if not instance.pk:
        pan_no = instance.pan_no
        email = instance.email or pan_no + '@anushree.com'
        user = User(email=email, username=pan_no.lower().replace('-', '_'),
                    password=instance.owner.split(' ')[0].lower() + '123', is_active=True,
                    first_name=instance.owner.split(' ')[0].capitalize() or None,
                    last_name=instance.owner.split(' ')[-1].capitalize() or None)

        user.save()

        group = Group.objects.get(name__iexact='customer')
        user.groups.add(group)

        instance.user = user
