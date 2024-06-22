from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from .models import CustomUser
# from .models import User
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'phone', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }





class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }



# reviews

 
# search_result

