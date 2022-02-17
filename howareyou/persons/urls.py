from django.urls import path
from . import views
app_name = 'persons'
urlpatterns = [
    path('', views.index, name='index'),
    path('patient_home/', views.patient_home, name='patient_home'),
]