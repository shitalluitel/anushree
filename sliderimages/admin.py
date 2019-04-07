from django.contrib import admin
from .models import SliderImage


# Register your models here.
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')


admin.site.register(SliderImage, SliderImageAdmin)
