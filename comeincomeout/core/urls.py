from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('report/', views.report_view, name='report'),
    path('register_time/', views.register_time_view, name='register_time'),
]
