
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import CheckInCheckOut
from .forms import CheckInForm, CheckOutForm, ReportFilterForm
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import csv

def check_in(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            check_in = form.save(commit=False)
            check_in.user = request.user
            check_in.check_in_time = timezone.now()
            check_in.save()
            return redirect('check_in')
    else:
        form = CheckInForm()
    return render(request, 'tracking/check_in.html', {'form': form})

@login_required
def check_out(request):
    if request.method == 'POST':
        form = CheckOutForm(request.POST)
        if form.is_valid():
            check_out = form.save(commit=False)
            check_out.user = request.user
            check_out.check_out_time = timezone.now()
            check_out.save()
            return redirect('check_out')
    else:
        form = CheckOutForm()
    return render(request, 'tracking/check_out.html', {'form': form})

@login_required
def report(request):
    form = ReportFilterForm(request.GET or None)
    records = CheckInCheckOut.objects.filter(user=request.user)
    
    if form.is_valid():
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        if date_from:
            records = records.filter(check_in_time__gte=date_from)
        if date_to:
            records = records.filter(check_out_time__lte=date_to)
    
    return render(request, 'tracking/report.html', {'form': form, 'records': records})

@login_required
def export_report_csv(request):
    records = CheckInCheckOut.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Check In Time', 'Check Out Time', 'Total Hours'])

    for record in records:
        writer.writerow([record.check_in_time, record.check_out_time, record.total_hours])
    
    return response

@login_required
def export_report_pdf(request):
    records = CheckInCheckOut.objects.filter(user=request.user)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Report about hours")
    p.drawString(100, 750, "Check IN | Check OUT | Total hours")

    y = 730
    for record in records:
        p.drawString(100, y, f"{record.check_in_time} | {record.check_out_time} | {record.total_hours}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, as_attachment=True, filename='report.pdf', content_type='application/pdf')