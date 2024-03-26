from django import forms


from .models import Patient


class PatientForm(forms.ModelForm):
    Patient_Name       = forms.CharField(label='Patient Name', widget=forms.TextInput(attrs={"placeholder": "Your Name"}))
    Age       = forms.DecimalField(widget=forms.TextInput(attrs={"placeholder": "Enter Age"}))              
    Patient_Location       = forms.CharField(label='Patient Location', widget=forms.TextInput(attrs={"placeholder": "Your Location"}))
    Phone_No       = forms.DecimalField(widget=forms.TextInput(attrs={"placeholder": "Enter Phone No"})) 
    Aadhar_No       = forms.DecimalField(widget=forms.TextInput(attrs={"placeholder": "Enter Aadhar No"}))        
    Address = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your Address",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 5,
                                    'cols': 50
                                }
                            )
                        )
    Email       = forms.CharField(label='Email', 
                    widget=forms.TextInput(attrs={"placeholder": "Your Email"}))                    
    Temperature       = forms.DecimalField(widget=forms.TextInput(attrs={"placeholder": "°F"}))
    Heart_Rate       = forms.DecimalField(widget=forms.TextInput(attrs={"placeholder": "BPM"}))
    BP_Value       = forms.DecimalField(widget=forms.TextInput(attrs={"placeholder": "mmHg"}))
    
    
    class Meta:
        model = Patient
        fields = [
            'Patient_Name',
            'Age',
            'Patient_Location',
            'Phone_No',
            'Aadhar_No',
            'Address',
            'Email',
            'Temperature',
            'Heart_Rate',
            'BP_Value'
        ]
   