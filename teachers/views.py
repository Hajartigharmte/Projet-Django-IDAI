
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Teacher
from home_auth.models import CustomUser  
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# LISTE DES PROFESSEURS
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

# AJOUTER UN PROFESSEUR  
@login_required
def add_teacher(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        qualification = request.POST.get('qualification')
        parcours = request.POST.get('parcours')
        
        try:
            # Création de l'utilisateur
            user = CustomUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=email
            )
            user.set_password("12345")
            user.save()

            # Création du professeur lié
            teacher = Teacher(
                admin=user, 
                teacher_id=email,
                first_name=first_name,
                last_name=last_name,
                photo=request.FILES.get('photo'),
                city=city,
                qualification=qualification,
                parcours=parcours,
                diploma="Master", 
                experience="2 ans",
                mobile_number="0600000000"
            )
            teacher.save()

            messages.success(request, f"Le professeur {first_name} a été ajouté !")
            return redirect('add_teacher')

        except Exception as e:
            messages.error(request, f"Erreur lors de l'envoi : {e}")
            
    return render(request, 'teachers/add_teacher.html')

# VUE DE DÉTAIL / RECHERCHE
def teacher_view(request, id=None):
    query = request.GET.get('search_name')
    teacher = None

    
    if id:
        teacher = get_object_or_404(Teacher, id=id)
    
    
    elif query:
        teacher = Teacher.objects.filter(
            Q(admin__first_name__icontains=query) | 
            Q(admin__last_name__icontains=query)
        ).first()

   
    return render(request, 'teachers/view_teacher.html', {
        'teacher': teacher, 
        'query': query
    })

# MODIFIER UN PROFESSEUR
@login_required
def edit_teacher(request, id=None): 
    teacher = None
    
   
    if id:
        teacher = get_object_or_404(Teacher, id=id)
    
    query = request.GET.get('search_name')
    if query:
        teacher = Teacher.objects.filter(
            Q(admin__first_name__icontains=query) | 
            Q(admin__last_name__icontains=query)
        ).first()

    if request.method == "POST" and teacher:
       
        teacher.admin.first_name = request.POST.get('first_name')
        teacher.admin.last_name = request.POST.get('last_name')
        teacher.admin.email = request.POST.get('email')
        teacher.admin.save()

        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.city = request.POST.get('city')
        teacher.qualification = request.POST.get('qualification')
        teacher.parcours = request.POST.get('parcours')
        
        if request.FILES.get('photo'):
            teacher.photo = request.FILES.get('photo')

        teacher.save()
        messages.success(request, f"Le profil de {teacher.first_name} a été mis à jour !")
        return redirect('teacher_list')

   
    return render(request, 'teachers/edit_teacher.html', {'teacher': teacher, 'query': query})

# SUPPRIMER UN PROFESSEUR
@login_required
def delete_teacher(request, id):
    # Utilisez get_object_or_404 pour éviter le NoneType
    teacher = get_object_or_404(Teacher, id=id)
    
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
        
    return redirect('teacher_list')
def teacher_dashboard(request):
    
    context = {
        'total_courses': 5,
        'total_students': 120,
        'upcoming_exams': 3,
        'total_hours': 48,
    }
    return render(request, 'teachers/teacher_dashboard.html', context)