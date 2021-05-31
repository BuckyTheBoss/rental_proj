from django import forms
from .models import Vehicle, VehicleSize, VehicleType


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['created_by'] 


class VehicleFormBasic(forms.Form):
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all())
    vehicle_size = forms.ModelChoiceField(queryset=VehicleSize.objects.all())
    real_cost = forms.FloatField()
    
