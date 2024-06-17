from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'address_line_1', 'address_line_2', 'city', 
            'state', 'postal_code', 'country'
        ]

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['address_line_1'].widget.attrs.update({'class': 'vTextField'})
        self.fields['address_line_2'].widget.attrs.update({'class': 'vTextField'})
        self.fields['city'].widget.attrs.update({'class': 'vTextField'})
        self.fields['state'].widget.attrs.update({'class': 'vTextField'})
        self.fields['postal_code'].widget.attrs.update({'class': 'vTextField'})
        self.fields['country'].widget.attrs.update({'class': 'vTextField'})
