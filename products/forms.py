from django import forms

class ProductFilterForm(forms.Form):
  name_search = forms.CharField(label="Name search", max_length=50, required=False)
  min_price=forms.DecimalField(label="min price search",decimal_places=2,required=False)
  max_price=forms.DecimalField(label="max price search",decimal_places=2,required=False)

