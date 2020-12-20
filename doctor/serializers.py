from rest_framework import serializers 
  
# import model from models.py 
from .models import Appointment 
from .models import Doctor
# Create a model serializer  
class AppointmentSerializer(serializers.ModelSerializer): 
    # specify model and fields 
    class Meta: 
        model = Appointment 
        # fields = ('patient_name','patient_age','date','timeslot','doctor')
        fields="__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"