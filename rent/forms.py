from django import forms
from django.forms.widgets import NumberInput
from .models import Vehicle, VehicleSize, VehicleType, Rental
from django.forms import formset_factory, modelformset_factory
from django .contrib.auth.forms import UserCreationForm


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['created_by'] 


class MyNumberInput(NumberInput):
    attrs={'class':'form-control'}


class VehicleFormBasic(forms.Form):
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    vehicle_size = forms.ModelChoiceField(queryset=VehicleSize.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    real_cost = forms.FloatField(widget=MyNumberInput())


    


VehicleFormSet = formset_factory(VehicleFormBasic, extra=3)

RentalModelFormSet = modelformset_factory(
   model=Rental,
   fields='__all__',
   extra=1
)


