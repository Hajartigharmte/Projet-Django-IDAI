
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Teacher
from home_auth.models import CustomUser  

#  LISTE DES PROFESSEURS
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

#  AJOUTER UN PROFESSEUR  
def add_teacher(request):
    if request.method == "POST":
        # Récupération des données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('date_of_birth')
        mobile = request.POST.get('mobile_number')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        address = request.POST.get('address')

        # Création de l'utilisateur
        user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,
            
        )
        user.set_password("12345") 
        user.save()

        # Création du profil Teacher lié à l'utilisateur
        teacher = Teacher(
            user=user,
            gender=gender,
            date_of_birth=dob,
            qualification=qualification,
            experience=experience,
            address=address
        )
        teacher.save()

        messages.success(request, "Professeur ajouté avec succès !")
        return redirect('teacher_list')

    return render(request, 'teachers/add_teacher.html')

def view_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    return render(request, 'teachers/view_teacher.html', {'teacher': teacher})

# Vue pour modifier un professeur
def edit_teacher(request, id):
    # 1. On récupère le professeur précis grâce à son ID
    teacher = get_object_or_404(Teacher, id=id)
    
    if request.method == "POST":
       
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        address = request.POST.get('address')

        
        teacher.user.first_name = first_name
        teacher.user.last_name = last_name
        teacher.user.email = email
        teacher.user.save()

        
        teacher.qualification = qualification
        teacher.experience = experience
        teacher.address = address
        teacher.save()

        messages.success(request, "Les modifications ont été enregistrées !")
        return redirect('teacher_list')

    
    return render(request, 'teachers/edit_teacher.html', {'teacher': teacher})

# Vue pour supprimer un professeur
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        user = teacher.user # On récupère l'utilisateur lié
        teacher.delete()    # On supprime le profil prof
        user.delete()       # On supprime le compte utilisateur
        return redirect('teacher_list')
    return redirect('teacher_list')