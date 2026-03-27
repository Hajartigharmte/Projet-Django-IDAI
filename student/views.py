from django.shortcuts import render


def student_list(request):
    return render(request, 'students/students.html')


def add_student(request):
    return render(request, 'students/add-student.html')

