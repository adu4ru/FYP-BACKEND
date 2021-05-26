import datetime
from time import timezone

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError

blood_group = [("1", "A+"), ("2", "A-"), ("3", "B+"), ("4", "B-"), ("5", "AB+"), ("6", "AB-"), ("3", "O+"), ("4", "O-")]
genderList = [("1", "Male"), ("2", "Female"), ("3", "Others")]
caseList = [("1", "Accident"), ("2", "Delivery"), ("3", "Anemia"), ("4", "Dialysis"), ("5", "Operation"),
            ("6", "Urgent"), ("7", "Others")]
hosiptaList = [("1", "BPKIHS"), ("2", "Vijaypur Hospital")]


class Event(models.Model):
    title = models.CharField(max_length=20)
    organiser_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    event_date = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'


class Register(models.Model):
    register_id = models.OneToOneField(User, on_delete=models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=genderList, max_length=2)
    address = models.CharField(max_length=50)
    number = models.PositiveIntegerField(unique=True)
    blood_group = models.CharField(choices=blood_group, max_length=2)
    image = models.ImageField(null=True, blank=True)
    last_donated_date = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    available_status = models.BooleanField(default=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    no_of_donations = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class BloodValidator(models.Model):
    request_id = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.request_id}'


class Blood(models.Model):
    register_id = models.ForeignKey(Register, null=True, blank=True, on_delete=models.DO_NOTHING)
    request_id = models.OneToOneField(BloodValidator, on_delete=models.DO_NOTHING, primary_key=True)
    patient_name = models.CharField(max_length=50)
    blood_group = models.CharField(choices=blood_group, max_length=2)
    gender = models.CharField(choices=genderList, max_length=2)
    number = models.PositiveIntegerField()
    case = models.CharField(choices=caseList, max_length=20)
    hospital = models.CharField(choices=hosiptaList, max_length=20)
    required_date = models.DateField()
    status = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if self.required_date < datetime.date.today():
    #         raise ValidationError("The date cannot be in the past!")
    #         return HttpResponse('Exception: DataNot Found')
    #
    #     #else:
    #         #except Exception as e:
    #         #return HttpResponse('Exception: DataNot Found')
    #
    #     #return HttpResponse(save)
    #             #self.message_user(request, 'Error changing model: %s' % e.msg, level=logging.ERROR)
    #
    #     super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.patient_name}'

    def save(self, *args, **kwargs):
        if self.required_date < datetime.date.today():
            raise ValidationError('Required date cannot be previous date', code='invalid')

        super(Blood, self).save(*args, **kwargs)


class Donation(models.Model):
    donor_id = models.ForeignKey(Register, on_delete=models.DO_NOTHING)
    request_id = models.ForeignKey(Blood, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Donations"
        unique_together = ['date', 'donor_id', 'request_id']

    def __str__(self):
        return f'{self.request_id}, {self.donor_id}'
