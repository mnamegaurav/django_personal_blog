from django.forms import ModelForm,TextInput, EmailInput, Textarea

from .models import ContactMeData, Article


class ContactMeDataForm(ModelForm):
    class Meta:
        model = ContactMeData

        fields = ('email', 'full_name', 'city', 'zip_code', 'say_something')

        widgets = {'email': EmailInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'inputEmail4', 'placeholder': 'Email'}),
                   'full_name': TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Full Name'}),
                   'city': TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'inputCity', 'placeholder': 'City'}),
                   'zip_code': TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'inputZip', 'placeholder': 'Zip'}),
                   'say_something': Textarea(attrs={'type': 'text', 'class': 'form-control', 'id': 'Textarea', 'placeholder': 'Say Something', 'style': 'height:100px'}), }