from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=64)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = "setting_type"
        verbose_name = "Type"
        verbose_name_plural = "Types"
