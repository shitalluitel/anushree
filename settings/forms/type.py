from django import forms

from settings.models.type import Type


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type

        fields = [
            'type',
        ]

        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'})
        }
