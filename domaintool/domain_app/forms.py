from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Company, Domain
from .models import User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
class UserForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'is_admin', 'is_user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #remove password2 option
        self.fields.pop('password2')

        # Set the help_text for password1 to an empty string to hide default messages
        self.fields['password1'].help_text = ""
        
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