from django import forms
from .models import Supplier



class TenderSearchForm(forms.Form):
    query = forms.CharField(label='Tender Reference', max_length=100)

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

