from django.db import models


class TradePattern(models.Model):
    trade_pattern = models.CharField(max_length=64)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.trade_pattern

    class Meta:
        db_table = "setting_trade_pattern"
        verbose_name = "Trade Pattern"
        verbose_name_plural = "Trade Patterns"
