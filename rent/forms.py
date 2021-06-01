from django import forms
from django.forms.widgets import NumberInput
from .models import Vehicle, VehicleSize, VehicleType
from django.forms import formset_factory

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['created_by'] 



class VehicleFormBasic(forms.Form):
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    vehicle_size = forms.ModelChoiceField(queryset=VehicleSize.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    real_cost = forms.FloatField(widget=NumberInput(attrs={'class':'form-control'}))


    
VehicleFormSet = formset_factory(VehicleFormBasic, extra=3)