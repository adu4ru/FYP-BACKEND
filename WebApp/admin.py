from django.contrib import admin
from .models import Register, Blood, Donation, Event, BloodValidator
admin.site.register(Event)
admin.site.register(BloodValidator)
# admin.site.register(Book_Appointment)
# Register your models here.
@admin.register(Blood)
class AdminBlood(admin.ModelAdmin):
    list_display= ['patient_name','blood_group','status']

@admin.register(Register)
class AdminRegister(admin.ModelAdmin):
    list_display= ['name','blood_group','available_status','is_verified']

@admin.register(Donation)
class AdminRegister(admin.ModelAdmin):
    list_display= ['donor_id','request_id','date','status']
