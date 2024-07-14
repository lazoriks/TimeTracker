from django.urls import path
from .views import LoginView, check_in_view, check_out_view, UserManagementView, report_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('check_in/', check_in_view, name='check_in'),
    path('check_out/', check_out_view, name='check_out'),
    path('user_management/', UserManagementView.as_view(), name='user_management'),
    path('report/', report_view, name='report'),
]