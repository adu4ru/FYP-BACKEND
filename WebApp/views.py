from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Register
from .models import Blood
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
        
        # if Register.objects.filter(userName=userName).exists():
        #     print('username taken')
            
        # elif Register.objects.filter(emailId=emailId).exists():
        #     print('Email Id exists')
        # else:
        user = User.objects.create(username=userName,email=emailId, password=password)
        register = Register.objects.create( register_id=user , name=name, gender=gender, address=address, number=number, bloodGroup=bloodGroup)
        #register= Register.objects.create(name=firstName, gender=gender, email=email, address=address,bloodGroup=bloodGroup, number=number, password=password)
        user.save()
        register.save()

            

    else:
        return render(request, 'Register.html')

    return HttpResponse("Done")

def blood(request):
    if request.method == 'POST':
        patientName = request.POST.get('patientName')
        gender = request.POST.get('gender')
        number = request.POST.get('number')
        hospital = request.POST.get('hospital')
        bloodGroup = request.POST.get('bloodGroup')
    
        blood = Blood.objects.create(patientName=patientName,gender=gender,number=number, hospital = hospital, bloodGroup=bloodGroup )
        blood.save()

    else:
        return render(request, 'Register.html')

    return HttpResponse("Done")