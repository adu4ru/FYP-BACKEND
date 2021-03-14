from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
from django.contrib.auth.models import User, auth
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        userName = request.POST.get('userName')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        number = request.POST.get('number')
        emailId = request.POST.get('emailId')
        bloodGroup = request.POST.get('bloodGroup')
        password = request.POST.get('password')
        
        if Register.objects.filter(userName=userName).exists():
            print('username taken')
            
        elif Register.objects.filter(emailId=emailId).exists():
            print('Email Id exists')
        else:
            register = Register.objects.create(name=name, userName=userName, gender=gender, emailId=emailId, address=address, number=number, bloodGroup=bloodGroup, password=password)
            #register= Register.objects.create(name=firstName, gender=gender, email=email, address=address,bloodGroup=bloodGroup, number=number, password=password)
            register.save()
            print(password)
            print(emailId)
            

    else:
        return render(request, 'Register.html')

    return HttpResponse("Done")
