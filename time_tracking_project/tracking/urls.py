# tracking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('check-in/', views.check_in, name='check_in'),
    path('check-out/', views.check_out, name='check_out'),
    path('report/', views.report, name='report'),
    path('export/csv/', views.export_report_csv, name='export_report_csv'),
    path('export/pdf/', views.export_report_pdf, name='export_report_pdf'),
]