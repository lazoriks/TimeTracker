from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import User, Hours
import pandas as pd
from io import StringIO
from django.template.loader import render_to_string
from weasyprint import HTML


def login_view(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=user, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('user_list')
        elif user is not None:
            return redirect('last_time')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def user_list_view(request):
    if not request.user.is_superuser:
        return redirect('login')
    try:
        users = User.objects.all()
    except Exception as e:
        return HttpResponse(f"Error retrieving users: {e}", status=500)
    return render(request, 'user_list.html', {'users': users})


def last_time_view(request):
    if request.method == 'POST':
        user = request.user
        date = request.POST['date']
        last_hour = Hours.objects.filter(user=user).order_by('-come_in').first()
        if last_hour and not last_hour.come_out:
            last_hour.come_out = date
            last_hour.hour = (last_hour.come_out - last_hour.come_in).total_seconds() / 3600
            last_hour.save()
        else:
            Hours.objects.create(user=user, come_in=date)
        return redirect('last_time')
    return render(request, 'last_time.html')


def report_view(request):
    if request.method == 'POST':
        start_period = request.POST.get('start_period')
        end_period = request.POST.get('end_period')
        user = request.POST.get('user')

        query = Hours.objects.all()
        if start_period:
            query = query.filter(come_in__gte=start_period)
        if end_period:
            query = query.filter(come_in__lte=end_period)
        if user:
            query = query.filter(user__user=user)

        hours = query

        if 'csv' in request.POST:
            csv_buffer = StringIO()
            df = pd.DataFrame(list(hours.values()))
            df.to_csv(csv_buffer, index=False)
            response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="report.csv"'
            return response

        if 'pdf' in request.POST:
            html_string = render_to_string('report_pdf.html', {'hours': hours})
            html = HTML(string=html_string)
            pdf = html.write_pdf()
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            return response

    return render(request, 'report.html')
