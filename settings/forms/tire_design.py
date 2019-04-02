from django import forms

from settings.models.tire_design import TireDesign


class TireDesignForm(forms.ModelForm):
    class Meta:
        model = TireDesign

        fields = [
            'tire_design',
        ]

        widgets = {
            'tire_design': forms.TextInput(attrs={'class': 'form-control'})
        }
