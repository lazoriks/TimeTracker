from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'password', 'superuser', 'email', 'mobile']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ReportForm(forms.Form):
    start_period = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_period = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
