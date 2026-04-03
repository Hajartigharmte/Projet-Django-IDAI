from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('add/', views.add_teacher, name='add_teacher'),
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('delete/<int:id>/', views.delete_teacher, name='delete_teacher'),

    # ROUTES POUR LA VUE (Détails/Recherche)
    path('view/', views.teacher_view, name='teacher_view'), # Pour le menu
    path('view/<int:id>/', views.teacher_view, name='teacher_view_details'), # Pour le tableau
    
    # ROUTES POUR L'ÉDITION
    path('edit/', views.edit_teacher, name='edit_teacher'), # Pour le menu
    path('edit/<int:id>/', views.edit_teacher, name='edit_teacher_form'), # Pour un ID précis
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
]