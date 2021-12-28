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
    path('patient', views.patient)
]
