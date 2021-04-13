from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


bloodgroup=[("1","A+"),("2","A-"),("3","B+"),("4","B-"),("5","AB+"),("6","AB-"),("3","O+"),("4","O-")]
genderList=[("1","Male"),("2","Female"),("3","Others")]
caseList=[("1","Accident"),("2","Delivery"),("3","Anemia"),("4","Dialysis"),("5","Operation"),("6","Others")]
hosiptaList=[("1","BPKIHS"),("2","Vijaypur Hospital")]
class Register(models.Model):
    register_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=50)
    # userName = models.CharField(max_length=20, unique=True)
    gender = models.CharField(choices=genderList, max_length=2)
    address = models.CharField(max_length=50)
    number = models.PositiveIntegerField(unique=True)
    # emailId = models.EmailField(max_length=50, unique=True)
    bloodGroup = models.CharField(choices=bloodgroup, max_length=2)
    # password = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.name}'
    

class Blood(models.Model):
    patientName = models.CharField(max_length=50)
    bloodGroup = models.CharField(choices=bloodgroup, max_length=2)
    gender = models.CharField(choices=genderList, max_length=2)
    number = models.PositiveIntegerField()
    requiredDate = models.DateField
    case = models.CharField(choices=caseList, max_length=20)
    hospital = models.CharField(choices=hosiptaList, max_length=20)
    
    
    def __str__(self):
        return f'{self.patientName}'
    

    