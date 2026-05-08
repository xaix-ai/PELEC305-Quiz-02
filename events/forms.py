from django import forms
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = "__all__"
        
        widgets = {
            'password': forms.PasswordInput()
        }
        
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        
        if len(full_name) < 5:
            raise forms.ValidationError("Full name must be atleast 5 characters long.")
        return full_name
    
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email mus be a valid Gmail address.")
        return email

    def clean_age(self):
        age = self.cleaned_data['age']
        
        if age < 18:
            raise forms.ValidationError("Your age must be at least 18 to register for the event")
        return age
    
    def clean_password(self):
        password = self.cleaned_data['password']
        
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        
        return password    
