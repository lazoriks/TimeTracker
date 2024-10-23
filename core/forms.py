from django import forms
from .models import User, Hours

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user', 'name', 'surname', 'password', 'super_user', 'email', 'mobile']

class HoursForm(forms.ModelForm):
    class Meta:
        model = Hours
        fields = ['user', 'come_in', 'come_out', 'hour']
