"""
URL configuration for time_tracking_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tracking import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Home page is set to the login page
    path('check_in/', views.CheckInView.as_view(), name='check_in'),
    path('check_out/', views.CheckOutView.as_view(), name='check_out'),
    path('user_management/', views.UserManagementView.as_view(), name='user_management'),
    path('report/', views.ReportView.as_view(), name='report'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)