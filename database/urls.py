from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='database-home'),
    path('about/', views.about, name='database-about'),
    path('add/1/', views.employee, name='employee'),
    path('add/2/', views.doctor_info, name='doctor-info'),
    path('add/3/', views.hospital_info, name='hospital-info'),
    path('add/4/', views.patient, name='patient'),
    path('add/5/', views.visit_info, name='visit-info'),
    path('add/6/', views.patient_info, name='patient-info'),
    path('add/7/', views.prescriptions, name='prescriptions'),
    path('add/8/', views.normalvalues, name='normalvalues'),
    path('add/9/', views.basic_tests, name='basic-tests'),
    path('add/10/', views.advanced_tests, name='advanced-tests'),
    path('add/11/', views.bmp_info, name='bmp-info'),
    path('add/12/', views.confirmation_tests, name='confirmation-tests')
]
