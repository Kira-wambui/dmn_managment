from django import forms
from .models import Company, Domain
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role_choices = [('admin', 'Admin'), ('user', 'User')]
    is_admin = forms.MultipleChoiceField(
        choices=role_choices,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'role-checkbox'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_admin', 'is_user']

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