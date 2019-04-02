from django import forms

from settings.models.trade_pattern import TradePattern


class TradePatternForm(forms.ModelForm):
    class Meta:
        model = TradePattern

        fields = [
            'trade_pattern',
        ]

        widgets = {
            'trade_pattern': forms.TextInput(attrs={'class': 'form-control'})
        }
