"""online_report URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from firereport.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('reporting/', reporting, name="reporting"),
    path('viewStatus/', viewStatus, name="viewStatus"),
    path('admin_login/', admin_login, name="admin_login"),
    path('dashboard/', dashboard, name="dashboard"),
    path('newRequest/', newRequest, name="newRequest"),
    path('allRequest/', allRequest, name="allRequest"),
    path('completeRequest/', completeRequest, name="completeRequest"),
    path('assignRequest/', assignRequest, name="assignRequest"),
    path('teamontheway/', teamontheway, name="teamontheway"),
    path('workinprogress/', workinprogress, name="workinprogress"),
    path('addTeam/', addTeam, name="addTeam"),
    path('manageTeam/', manageTeam, name="manageTeam"),
    path('dateReport/', dateReport, name="dateReport"),
    path('search/', search, name="search"),
    path('changePassword/', changePassword, name="changePassword"),
    path('viewStatusDetails/<int:id>', viewStatusDetails, name="viewStatusDetails"),
    path('viewRequestDetails/<int:id>', viewRequestDetails, name="viewRequestDetails"),
    path('deleteRequest/<int:id>', deleteRequest, name="deleteRequest"),
    path('editTeam/<int:id>', editTeam, name="editTeam"),
    path('deleteTeam/<int:id>', deleteTeam, name="deleteTeam"),

    path('logout/', Logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
