from django.db import models


class TireDesign(models.Model):
    tire_design = models.CharField(max_length=64)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tire_design

    class Meta:
        db_table = "setting_tire_design"
        verbose_name = "Tire Design"
        verbose_name_plural = "Tire Designs"
