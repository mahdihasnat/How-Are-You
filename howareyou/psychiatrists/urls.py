from django.urls import path
from . import views
app_name = 'psychiatrists'
urlpatterns = [
	path('psychiatrist_home', views.psychiatrist_home, name='psychiatrist_home'),
	path('test_result_poll', views.test_result_poll, name='test_result_poll'),
]