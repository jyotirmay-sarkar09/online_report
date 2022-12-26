from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'home.html')

def reporting(request):
    if request.method == "POST":
        FullName = request.POST['FullName']
        MobileNumber = request.POST['MobileNumber']
        Location = request.POST['Location']
        Message = request.POST['Message']
        try:
            Firereport.objects.create(FullName=FullName, MobileNumber=MobileNumber, Location=Location, Message=Message)
            error= "no"
        except:
            error = "yes"
    return render(request, 'reporting.html', locals())

def viewStatus(request):
    if request.method == "POST":
        sd = request.POST['searchdata']
        print(sd)
        try:
            firereport = Firereport.objects.filter(Q(FullName__icontains=sd) | Q(MobileNumber=sd) | Q(Location__icontains=sd))
        except:
            firereport = ""
       
    return render(request, "viewStatus.html", locals())

def admin_login(request):
    pass

def viewStatusDetails(request, id):
    pass