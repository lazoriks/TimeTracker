from django.shortcuts import render, redirect
from .models import User, Hours
from .forms import UserForm, ReportForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            if user.superuser:
                return redirect('dashboard')
            else:
                return redirect('register_time')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

def dashboard_view(request):
    users = User.objects.all()
    return render(request, 'core/dashboard.html', {'users': users})

def report_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            start_period = form.cleaned_data['start_period']
            end_period = form.cleaned_data['end_period']
            user = form.cleaned_data['user']
            hours = Hours.objects.filter(come_in__range=(start_period, end_period))
            if user:
                hours = hours.filter(user=user)
            return render(request, 'core/report.html', {'form': form, 'hours': hours})
    else:
        form = ReportForm()
    return render(request, 'core/report.html', {'form': form})

from django.utils import timezone

def register_time_view(request):
    user = User.objects.get(id=request.session['user_id'])
    last_record = Hours.objects.filter(user=user).order_by('-come_in').first()
    now = timezone.now()
    
    if last_record and not last_record.come_out:
        message = "Last Come In"
        last_record.come_out = now
        last_record.hours = (last_record.come_out - last_record.come_in).total_seconds() / 3600.0
        last_record.save()
    else:
        message = "Last Come Out"
        Hours.objects.create(user=user, come_in=now)

    return render(request, 'core/register_time.html', {'message': message, 'date': now})


