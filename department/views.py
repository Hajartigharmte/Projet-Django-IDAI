from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Department
from teachers.models import Teacher
from django.contrib.auth.decorators import login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/department-list.html', {'departments': departments})
@login_required
def add_department(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        head_id = request.POST.get('head')
        teacher_ids = request.POST.getlist('teachers')

        head = Teacher.objects.get(id=head_id) if head_id else None
        department = Department.objects.create(name=name, description=description, head=head)
        for tid in teacher_ids:
            department.teachers.add(tid)

        messages.success(request, "Department added successfully!")
        return redirect('department_list')

    return render(request, 'departments/add-department.html', {'teachers': teachers})
@login_required
def edit_department(request, dept_id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    department = get_object_or_404(Department, id=dept_id)
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        head_id = request.POST.get('head')
        teacher_ids = request.POST.getlist('teachers')

        department.head = Teacher.objects.get(id=head_id) if head_id else None
        department.save()
        department.teachers.set(teacher_ids)

        messages.success(request, "Department updated successfully!")
        return redirect('department_list')

    return render(request, 'departments/edit-department.html', {'department': department, 'teachers': teachers})
@login_required
def delete_department(request, dept_id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    department = get_object_or_404(Department, id=dept_id)
    department.delete()
    messages.success(request, "Department deleted successfully!")
    return redirect('department_list')