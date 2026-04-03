
from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, Grade
from .forms import ExamForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


def exam_list(request):
    exams = Exam.objects.all().order_by('exam_date')
    return render(request, 'exams/exam_list.html', {'exams': exams})


def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'exams/add_exam.html', {'form': form})

User = get_user_model()
@login_required

def enter_results(request, exam_id):
    is_teacher = request.user.groups.filter(name='Teachers').exists()
    
    if request.user.is_superuser or is_teacher:
        exam = get_object_or_404(Exam, id=exam_id)
        
        students = User.objects.filter(is_student=True)
        if request.method == 'POST':
            for student in students:
                score = request.POST.get(f'score_{student.id}')
                if score:
                    Grade.objects.update_or_create(
                        exam=exam,
                        student=student,
                        defaults={'score': score}
                    )
            return redirect('exam_list')
            
        return render(request, 'exams/enter_results.html', {
            'exam': exam,
            'students': students
        })
    return redirect('dashboard')
