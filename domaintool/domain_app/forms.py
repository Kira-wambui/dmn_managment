from django import forms
from .models import Company, Domain


class CompanyForm(forms.ModelForm):
    
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            'name': 'Company Name',
            'address': 'Company Address',
            'location': 'Company Location',
        }
        

class DomainForm(forms.ModelForm):
    
    class Meta:
        model = Domain
        fields = '__all__'
        labels = {
            'name': 'Domain Name',
            'registration_date': 'Date of Registration',
            'expiry_date': 'Date of Expiry',
            'company': 'Belongs To(Company):'
        }