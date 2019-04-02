from django import forms

from settings.models.trade_mark import TradeMark


class TradeMarkForm(forms.ModelForm):
    class Meta:
        model = TradeMark

        fields = [
            'trade_mark',
        ]

        widgets = {
            'trade_mark': forms.TextInput(attrs={'class': 'form-control'})
        }
