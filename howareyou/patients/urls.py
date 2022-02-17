from django.urls import path

from . import views

app_name = "patients"
urlpatterns = [
	path('patient_home', views.patient_home, name='patient_home'),
]