from django.db import models


class TradeMark(models.Model):
    trade_mark = models.CharField(max_length=64)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.trade_mark

    class Meta:
        db_table = "setting_trade_mark"
        verbose_name = "Trade Mark"
        verbose_name_plural = "Trade Marks"
