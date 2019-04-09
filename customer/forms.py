from django import forms
from django.contrib.auth import password_validation

from customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = [
            'owner',
            'company',
            'address',
            'mobile_no',
            'phone_no',
            'email',
            'pan_no',
        ]

        widgets = {
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_no': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'owner': 'Owner Name',
            'company': 'Company Name',
            'address': 'Address',
            'mobile_no': 'Mobile Number',
            'phone_no': 'Phone Number',
            'email': 'Email',
            'pan_no': 'PAN Number',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone_no'].required = False
        self.fields['email'].required = False


class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your new password'}),
        strip=False,
    )

    confirm_new_password = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your new password password'}),
        strip=False,
    )

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']
        if new_password and confirm_new_password:
            if new_password != confirm_new_password:
                raise forms.ValidationError('Password mismatch')
        return confirm_new_password
