from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import CheckInCheckOut
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckInCheckOut
        fields = ['check_in_time']
        widgets = {'check_in_time': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'})}

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckInCheckOut
        fields = ['check_out_time']
        widgets = {'check_out_time': forms.DateTimeInput(attrs={'class': 'form-control'})}

class UserManagementForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_staff = forms.BooleanField(required=False, initial=False)
    is_superuser = forms.BooleanField(required=False, initial=False)

class ReportForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))