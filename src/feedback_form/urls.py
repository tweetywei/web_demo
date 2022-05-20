from django.urls import path, re_path
from . import views

app_name = 'feedback_form'
urlpatterns = [
    re_path(r'^$', views.feedback_form, name='home'),
]