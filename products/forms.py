from django import forms

from categories.models import Category
from products.models import Product


class TubeForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            'pattern_name',
            'pattern_code',
            'size',
            # 'category',
            # 'product_name',
            'stock',
            'price',
        ]

        widgets = {
            'pattern_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pattern_code': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            # 'product_name': forms.TextInput(attrs={'class': 'form-control'}),

            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #
        #     self.fields['category'].queryset = Category.objects.filter(is_deleted=False)


class TyreForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            'size',
            'product_name',
            # 'category',
            'pr',
            'stock',
            'price',
        ]

        widgets = {
            'pr': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),

            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        # def __init__(self, *args, **kwargs):
            # super().__init__(*args, **kwargs)
            #
            # self.fields['category'].queryset = Category.objects.filter(is_deleted=False)


class TubeEditForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            'pattern_name',
            'pattern_code',
            'size',
            'price',
        ]

        widgets = {
            'pattern_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pattern_code': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #
        #     self.fields['category'].queryset = Category.objects.filter(is_deleted=False)


class TyreEditForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            'size',
            'product_name',
            'pr',
            'price',
        ]

        widgets = {
            'pr': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        #
        # self.fields['category'].queryset = Category.objects.filter(is_deleted=False)
