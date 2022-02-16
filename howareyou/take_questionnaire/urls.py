# from django.contrib import admin
# from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.take_questionnaire, name='take_questionnaire'),
]
