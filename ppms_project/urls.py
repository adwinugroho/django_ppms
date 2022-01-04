from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about', views.about),
    path('faq', views.faq),
    # run when submit patient
    path('input-data', views.submitPatient, name='input_data'),
    path('patient', views.patient),
    path('print-data', views.printData, name='print_data'),
    path('submit-measurement', views.submitMeasurement, name='submit_measurement'),
    path('logout', views.logout, name='logout'),
    path('front-faq', views.frontFaq)
]
