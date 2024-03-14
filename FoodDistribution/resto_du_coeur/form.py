from .models import *
from django import  forms
#from authentification_app.models import UserRegistrationModel

class AddPrductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('image',)

# class UserPrductForm(forms.ModelForm):
#     class Meta:
#         model = UserRegistrationModel
#         exclude = ('password', 'permissions', 'groups', )