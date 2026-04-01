from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('add/', views.add_exam, name='add_exam'),
    path('enter-results/<int:exam_id>/', views.enter_results, name='enter_results'),
    
]