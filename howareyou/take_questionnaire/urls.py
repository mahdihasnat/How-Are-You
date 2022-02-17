# from django.contrib import admin
# from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_a_test, name='render_a_test'),
    path('submit', views.render_submitted, name='render_submitted'),
]
