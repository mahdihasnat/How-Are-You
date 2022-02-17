# from django.contrib import admin
# from django.urls import path
from django.urls import path

from . import views
app_name = 'take_questionnaire'
urlpatterns = [
    path('', views.render_test, name='render_test'),
    path('submit/', views.render_submit, name='render_submit'),

]
