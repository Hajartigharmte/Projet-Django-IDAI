# faculty/views.py 
from django.shortcuts import render 
from django.http import HttpResponse 
 
def index(request): 
    # return HttpResponse('First test')  ← remplacé par : 
    return render(request, 'Home/index.html')