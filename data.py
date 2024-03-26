from django import forms
from .models import Testing
import random


class TestingForm(forms.ModelForm):
    Temperature1       = forms.DecimalField(initial=random.randrange(96,106),  widget=forms.TextInput(attrs={"placeholder": "°F"}))
    Heart_Rate1       = forms.DecimalField(initial=random.randrange(50,100), widget=forms.TextInput(attrs={"placeholder": "BPM"}))
    BP_Rate1       = forms.DecimalField(initial=random.randrange(120,140), widget=forms.TextInput(attrs={"placeholder": "mmHg"}))
    

    class Meta:
        model = Testing
        fields = [
            'Temperature1',
            'Heart_Rate1',
            'BP_Rate1'
        ]

    def clean_Temperature1(self, *args, **kwargs):
    	Temperature1 = self.cleaned_data.get("Temperature1")
    	if Temperature1>100:
    		return Temperature1
    	else:
    		raise forms.ValidationError("Temperature is Normal") 

    def clean_Heart_Rate1(self, *args, **kwargs):
    	Heart_Rate1 = self.cleaned_data.get("Heart_Rate1")
    	if Heart_Rate1>102:
    		return Heart_Rate1
    	else:
    		raise forms.ValidationError("Heart Rate is Normal") 

    def clean_BP_Rate1(self, *args, **kwargs):
    	BP_Rate1 = self.cleaned_data.get("BP_Rate1")
    	if BP_Rate1>125:
    		return BP_Rate1
    	else:
    		raise forms.ValidationError("Normal BP ") 

	
    
  