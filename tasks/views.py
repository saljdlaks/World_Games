from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def home(request):
   return render(request,'home.html')

def signup(request):


    if request.method == 'GET':
        return render(request, 'signup.html',
    {
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password1']:
             try:
                user = User.objects.create_user(usermame = request.POST['username'],
                password = request.POST['password1'])
                User.save()
                return HttpResponse('User created successfully')
             except:
                return HttpResponse('Username alreday exists')
        return HttpResponse('Password do not match')
    

   