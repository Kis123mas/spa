from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
import re

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserRegistrationForm, self).__init__(*args, **kwargs)

        # Add class to form fields for consistent styling
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'id': 'email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password',
            'id': 'password1'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password',
            'id': 'password2'
        })

        # Update field labels
        self.fields['email'].label = "Email Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Check if the email is already in use
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered.")
        
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Ensure that password1 and password2 match
        if password1 != password2:
            raise ValidationError("The two password fields must match.")
        
        # Validate password strength (optional)
        password_strength = self.check_password_strength(password1)
        if not password_strength:
            raise ValidationError("Password must contain at least 8 characters, including both letters and numbers.")

        return password2

    def check_password_strength(self, password):
        """ Check if the password contains at least one letter and one number, and is at least 8 characters long. """
        if len(password) < 8:
            return False
        if not re.search(r'[a-zA-Z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        return True
