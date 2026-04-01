from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from teachers.models import Teacher
from department.models import Department
from django.contrib.auth.decorators import login_required

#  LISTE DES MATIÈRES
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})

#  AJOUTER UNE MATIÈRE
@login_required
def add_subject(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    teachers = Teacher.objects.all() 
    departments = Department.objects.all()
    
    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        teacher_id = request.POST.get('teacher')
        dept_id = request.POST.get('department')
        
        teacher = Teacher.objects.get(id=teacher_id)
        department = Department.objects.get(id=dept_id)
        
        Subject.objects.create(
            subject_name=subject_name,
            teacher=teacher,
            department=department
        )
        return redirect('subject_list')
        
    return render(request, 'subjects/add_subject.html', {'teachers': teachers ,'departments': departments})

#  MODIFIER UNE MATIÈRE
@login_required
def edit_subject(request, id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    subject = get_object_or_404(Subject, id=id)
    teachers = Teacher.objects.all()
    
    if request.method == "POST":
        subject.subject_name = request.POST.get('subject_name')
        teacher_id = request.POST.get('teacher')
        subject.teacher = Teacher.objects.get(id=teacher_id)
        subject.save()
        return redirect('subject_list')
        
    return render(request, 'subjects/edit_subject.html', {'subject': subject, 'teachers': teachers})

@login_required
def delete_subject(request, id):
    if not request.user.is_superuser:
        return redirect('home')
    subject = get_object_or_404(Subject, id=id)
    subject.delete()
    return redirect('subject_list')