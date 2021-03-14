from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


bloodgroup=[(1,"A+"),(2,"A-"),(3,"B+"),(4,"B-")]
genderList=[("1","Male"),("2","Female"),("3","Others")]

# class AccountManager(AbstractBaseUser):
#     def create_user(self, name, emailId, gender, password):
#         if not name:
#             raise ValueError("Enter name")
#         if not emailId:
#             raise ValueError("Enter Email")

#         user = self.model(
#             email=self.normalize_email(emailId),
#             userName=name,
#         )

#         user.set_password(password)
#         user.save(user=self._db)
#         return user

    

class Register(models.Model):

    name = models.CharField(max_length=50)
    userName = models.CharField(max_length=20, unique=True)
    gender = models.CharField(choices=genderList, max_length=2)
    address = models.CharField(max_length=50)
    number = models.PositiveIntegerField(unique=True)
    emailId = models.EmailField(max_length=50, unique=True)
    bloodGroup = models.CharField(choices=bloodgroup, default=1, max_length=2)
    password = models.CharField(max_length=14)
    # is_admin =models.BooleanField(default=False)
    # is_active =models.BooleanField(default=True)
    # is_staff =models.BooleanField(default=False)
    # is_superuser =models.BooleanField(default=False)

    # USERNAME_FIELD ="emailId"
    # REQUIRED_FIELDS=['name','userName','gender','address','number','emailId','bloodGroup','password']

    # objects = AccountManager()
    # def __str__(self):
    #     return self.name
    
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    
    # def has_module_perms(self, app_label):
    #     return True

class Blood(models.Model):
    patientName = models.CharField(max_length=50)
    gender = models.CharField(choices=genderList, max_length=2)
    number = models.PositiveIntegerField()
    hospital = models.CharField(max_length=25)
    bloodGroup = models.CharField(choices=bloodgroup, default=1, max_length=2)

    