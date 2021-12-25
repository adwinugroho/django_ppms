from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('dashboard', views.dashboard),
    path('about', views.about),
    path('faq', views.faq),
    path('patient', views.patient)
]
