from django.db import models
#from datetimewidget.widgets import DateTimeWidget
# Create your models here.

class Doctor(models.Model):
    department = (
        ('Dentistry', "Dentistry"),
        ('Cardiology', "Cardiology"),
        ('ENT Specialists', "ENT Specialists"),
        ('Astrology', 'Astrology'),
        ('Neuroanatomy', 'Neuroanatomy'),
        ('Blood Screening', 'Blood Screening'),
        ('Eye Care', 'Eye Care'),
        ('Physical Therapy', 'Physical Therapy'),
    )
    username=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    speciality=models.CharField(choices=department,max_length=100)

    
    

class Patient(models.Model):
    username=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()


class Appointment(models.Model):

    class Meta:
        unique_together=('doctor','date','timeslot')
        
        #unique_together=('patient','date','timeslot')
    # TIMESLOT_LIST=(
    #     (0,'09:00-10:00'),
    #     (1,'10:00-11:00'),
    #     (2,'11:00-12:00'),
    #     (3,'12:00-13:00'),
    #     (4,'13:00-14:00'),
    #     (5,'14:00-15:00'),
    #     (6,'15:00-16:00'),
    #     (7,'16:00-17:00'),
    # )
    TIMESLOT_LIST=(
        ('09:00-10:00','09:00-10:00'),
        ('10:00-11:00','10:00-11:00'),
        ('11:00-12:00','11:00-12:00'),
        ('12:00-13:00','12:00-13:00'),
        ('13:00-14:00','13:00-14:00'),
        ('14:00-15:00','14:00-15:00'),
        ('15:00-16:00','15:00-16:00'),
        ('16:00-17:00','16:00-17:00'),
    )

    #from models import Doctor.username
    #patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=100,default="noname")
    patient_age=models.IntegerField(default=1)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    
    #doctorname=doctor.name(default="Ram")
    timeslot=models.CharField(choices=TIMESLOT_LIST,max_length=100)
    date=models.DateField()

