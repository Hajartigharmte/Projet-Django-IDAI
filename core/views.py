from django.shortcuts import render, redirect
from .models import TimeTable, Holiday, Department, Teacher, Subject

# Création emploi du temps
def create_timetable(request):
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        TimeTable.objects.create(
            department_id=request.POST.get('department'),
            teacher_id=request.POST.get('teacher'),
            subject_id=request.POST.get('subject'),
            day_of_week=request.POST.get('day_of_week'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time')
        )
        return redirect('list_timetable')

    return render(request, 'timetable/create_timetable.html', {
        'departments': departments,
        'teachers': teachers,
        'subjects': subjects
    })


def list_timetable(request):
    departments = Department.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'timetable/timetable_list.html', {'departments': departments, 'subjects': subjects})


def holidays_list(request):
    holidays = Holiday.objects.all().order_by('start_date')
    return render(request, 'holidays/holiday_list.html', {'holidays': holidays})