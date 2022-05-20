from django.urls import path, re_path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('courses/<int:course_id>', views.dashboard, name='course_detail'),
    path('courses', views.course_list, name='course_list'),
]