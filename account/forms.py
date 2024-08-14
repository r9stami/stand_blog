from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User, Contact


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["phone","email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone","email", "password", "first_name"
            ,"last_name", "is_active", "is_admin"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        labels = {
            'full_name':'Full Name',
            'email':'Email',
            'phone':'Phone Number',
            'message':'Message',
        }


class LoginForm(forms.Form):
    phone = forms.CharField(label='Phone Number',widget=forms.TextInput)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','phone','email','password']
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'phone':'Phone Number',
            'email':'Email',
            'password':'Password'

        }



class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','phone','email','password','image']

        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'phone':'Phone Number',
            'email':'Email',
            'password':'Password',
            'image':'Image',

        }