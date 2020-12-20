from django.shortcuts import render

from .forms import AppointmentForm
from .forms import DoctorForm
from .models import Appointment

from rest_framework import viewsets
from .serializers import *

#create a viewset
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class= AppointmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

# Create your views here.
def index(request):
    return render(request,"home.html")

def appointment(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"success.html")
        else:
            return render(request,"fail.html")
    else:
        context={}
        context['form']=AppointmentForm()
        return render(request,"appointment.html",context)

def doctor(request):
    if request.method=='POST':
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            #users=Doctor.objects.all()
            context={}
            return render(request,"success.html")
        else:
            return render(request,"fail.html")
    else:
        context={}
        context['form']=DoctorForm()
        return render(request,"doctor.html",context)
    
def display(request):
    context={}
    context['appointment']=Appointment.objects.all()
    return render(request,"display.html",context)
