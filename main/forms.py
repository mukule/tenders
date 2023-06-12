from django import forms
from .models import Supplier
from django.conf import settings
import pycountry


class TenderSearchForm(forms.Form):
    query = forms.CharField(label='Tender Reference', max_length=100)


class SupplierForm(forms.ModelForm):
    language = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    currency = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    country = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['language'].choices = self.get_language_choices()
        self.fields['currency'].choices = self.get_currency_choices()
        self.fields['country'].choices = self.get_country_choices()

    def get_language_choices(self):
        languages = settings.LANGUAGES
        return languages

    def get_currency_choices(self):
        currencies = [(currency.alpha_3, f"{currency.alpha_3} - {currency.name}") for currency in pycountry.currencies]
        return currencies

    def get_country_choices(self):
        countries = [(country.alpha_2, country.name) for country in pycountry.countries]
        return countries

    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'duns_number': forms.TextInput(attrs={'class': 'form-control'}),
            'tax_jurisdiction_code': forms.TextInput(attrs={'class': 'form-control'}),
            'vendor_category': forms.Select(attrs={'class': 'form-control'}),
            'product_category': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'region_district': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'company_postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'building': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'function': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }