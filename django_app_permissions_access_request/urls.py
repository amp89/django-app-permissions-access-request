"""access_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django_app_permissions_access_request import views

urlpatterns = [
    
    path('approvals/', views.ApprovalsView.as_view(), name='django_app_permissions_access_request.approvals'),
    path('approval/', views.ApprovalView.as_view(), name='django_app_permissions_access_request.approval'),
    path('deny/', views.DenyView.as_view(), name='django_app_permissions_access_request.deny'),

    path('request/', views.RequestView.as_view(), name='django_app_permissions_access_request.request_access'),
    path('', views.RequestListView.as_view(), name='django_app_permissions_access_request.request_list'),
]

