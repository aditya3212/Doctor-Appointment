#from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index

from rest_framework import routers

from .views import *

router=routers.DefaultRouter()
router.register(r'appointmentt',AppointmentViewSet)
router.register(r'doctorr',DoctorViewSet)

urlpatterns = [
    
    path('',views.index),
    path('appointment',views.appointment),
    path('doctor',views.doctor),
    path('display',views.display),

    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]