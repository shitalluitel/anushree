from django.contrib import admin

# Register your models here.
from .models import TireDesign, TradeMark, TradePattern, Type

admin.site.register(TireDesign)
admin.site.register(TradeMark)
admin.site.register(TradePattern)
admin.site.register(Type)
