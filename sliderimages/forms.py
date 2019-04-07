from django import forms

from sliderimages.models import SliderImage


class SliderImageForm(forms.ModelForm):
    class Meta:
        model = SliderImage

        fields = [
            'name',
            'description',
            'image',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
