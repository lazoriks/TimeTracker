from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import CheckInCheckOut

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
    
class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckInCheckOut
        fields = ['check_in_time']

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['check_in_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckInCheckOut
        fields = ['check_out_time']

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['check_out_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})

    def clean(self):
        cleaned_data = super().clean()
        check_in_time = cleaned_data.get("check_in_time")
        check_out_time = cleaned_data.get("check_out_time")

        if check_out_time and check_in_time and check_out_time <= check_in_time:
            raise forms.ValidationError("The exit time must be later than the entry time.")