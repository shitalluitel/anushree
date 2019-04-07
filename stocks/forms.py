from django import forms

from products.models import Product
from stocks.models import Stock


class TireStockForm(forms.ModelForm):
    class Meta:
        model = Stock

        fields = [
            'item',
            'quantity',
        ]

        widgets = {
            'item': forms.Select(attrs={'class': 'form-control select2'}),
            'quantity': forms.NumberInput(attrs={'class': "form-control"})
        }

        labels = {
            'item': 'Item',
            'quantity': 'Stock'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['item'].queryset = Product.objects.filter(category__name__icontains='tire', is_deleted=False)


class TubeStockForm(TireStockForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['item'].queryset = Product.objects.filter(category__name__icontains='tube', is_deleted=False)
