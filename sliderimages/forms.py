import os

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from sliderimages.models import SliderImage


class SliderImageForm(forms.ModelForm):
    class Meta:
        model = SliderImage

        fields = [
            'image',
            'description',
            'name',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean(self):
        image = self.cleaned_data.get('image')
        extension = os.path.splitext(image.name)[1]
        if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            return self.cleaned_data

        raise ValidationError(_("Invalid file format. Image must be one of these [ .jpg, .jpeg, .png or .gif ]. "))
