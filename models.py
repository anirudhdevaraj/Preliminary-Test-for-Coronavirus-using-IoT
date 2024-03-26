from django.db import models




class Patient(models.Model):
    Patient_Name       = models.CharField(max_length=120) # max_length = required
    Age      = models.DecimalField(decimal_places=2, max_digits=10000)
    Patient_Location       = models.CharField(max_length=120) # max_length = required
    Phone_No      = models.DecimalField(decimal_places=2, max_digits=10000)
    Aadhar_No      = models.DecimalField(decimal_places=2, max_digits=10000)
    Address = models.TextField(blank=True, null=True)
    Email       = models.CharField(max_length=120) # max_length = required
    Temperature      = models.DecimalField(decimal_places=2, max_digits=10000)
    Heart_Rate      = models.DecimalField(decimal_places=2, max_digits=10000)
    BP_Value      = models.DecimalField(decimal_places=2, max_digits=10000)

	
class Testing(models.Model):
	Temperature1      = models.DecimalField(decimal_places=2, max_digits=10000)
	Heart_Rate1      = models.DecimalField(decimal_places=2, max_digits=10000)
	BP_Rate1      = models.DecimalField(decimal_places=2, max_digits=10000)
   