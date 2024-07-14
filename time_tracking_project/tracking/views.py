from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import LoginForm, CheckInForm, CheckOutForm, UserManagementForm, ReportForm
from .models import CheckInCheckOut
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User  # Import User model here

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('user_management')
                else:
                    # Redirect to the check-in or check-out page based on check-in status
                    check_in_record = CheckInCheckOut.objects.filter(user=user, check_out_time__isnull=True).first()
                    if check_in_record:
                        return redirect('check_out')
                    else:
                        return redirect('check_in')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'tracking/login.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CheckInView(View):
    def get(self, request):
        form = CheckInForm()
        return render(request, 'tracking/check_in.html', {'form': form})

    def post(self, request):
        form = CheckInForm(request.POST)
        if form.is_valid():
            check_in_time = form.cleaned_data['check_in_time']
            CheckInCheckOut.objects.create(user=request.user, check_in_time=check_in_time)
            return redirect('check_out')
        return render(request, 'tracking/check_in.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CheckOutView(View):
    def get(self, request):
        form = CheckOutForm()
        return render(request, 'tracking/check_out.html', {'form': form})

    def post(self, request):
        form = CheckOutForm(request.POST)
        if form.is_valid():
            check_out_time = form.cleaned_data['check_out_time']
            check_in_record = CheckInCheckOut.objects.filter(user=request.user, check_out_time__isnull=True).first()
            if check_in_record:
                check_in_record.check_out_time = check_out_time
                check_in_record.save()
                return redirect('check_in')
            else:
                form.add_error(None, 'No active check-in record found.')
        return render(request, 'tracking/check_out.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserManagementView(View):
    def get(self, request):
        form = UserManagementForm()
        return render(request, 'tracking/user_management.html', {'form': form})

    def post(self, request):
        form = UserManagementForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            is_staff = form.cleaned_data['is_staff']
            is_superuser = form.cleaned_data['is_superuser']
            user = User.objects.create_user(email=email, password=password, is_staff=is_staff, is_superuser=is_superuser)
            return redirect('user_management')
        return render(request, 'tracking/user_management.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ReportView(View):
    def get(self, request):
        form = ReportForm()
        return render(request, 'tracking/report.html', {'form': form})
    def post(self, request):
        form = ReportForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Add logic to generate and export the report
            return redirect('report')
        return render(request, 'tracking/report.html', {'form': form})
    