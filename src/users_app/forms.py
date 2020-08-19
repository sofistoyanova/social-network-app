from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout

user = get_user_model()

class SigninForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Wrong username or password')
        return self.cleaned_data


class SignupForm(forms.ModelForm):
        #email = forms.EmailField()
        password=forms.CharField(widget=forms.PasswordInput())
        confirm_password=forms.CharField(widget=forms.PasswordInput())
        class Meta:
            model = User
            fields = ['email', 'username', 'password']

        def clean(self):
            # validate email
            email = self.cleaned_data['email']
            existing_email_qs = User.objects.filter(email=email)
            if existing_email_qs.exists():
                raise forms.ValidationError('Email already exists')

            username = self.cleaned_data['username']
            existing_username_qs = User.objects.filter(username=username)
            if existing_username_qs.exists():
                raise forms.ValidationError('Username already exists')

            # validate password
            password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirm_password']
            if password != confirm_password:
                raise forms.ValidationError('Passwords are not the same')
