from django import forms


class TenderSearchForm(forms.Form):
    query = forms.CharField(label='Tender Reference', max_length=100)
