from django.urls import path
from . import views

urlpatterns = [
    path('holidays/', views.holidays_list, name='holidays_list'),
    path('timetable/create/', views.create_timetable, name='create_timetable'),
    path('timetable/', views.list_timetable, name='list_timetable'),
]