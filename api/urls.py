from django.urls import path
from .views import UserRecordView, BloodRecordView, RegisterRecordView, DonationRecordView, EventRecordView,BloodValidatorRecordView, ListDonorRecord, SetAvailabilityRecordView, SetLatitudeLongitudeRecordView, SetLastDonatedDateRecordView, SetPictureRecordView
app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('register/', RegisterRecordView.as_view(), name='register'),
    path('blood/', BloodRecordView.as_view(), name='blood'),
    path('donation/', DonationRecordView.as_view(), name='donation'),
    path('event/', EventRecordView.as_view(), name='event'),
    path('BloodValidator/', EventRecordView.as_view(), name='BloodValidator'),
    path('list-of-donors/<str:blood_group>', ListDonorRecord.as_view(), name='ListOfDonors'),
    path('available-status/', SetAvailabilityRecordView.as_view(), name='AvailabilityStatus'),
    path('set-lat-long/', SetLatitudeLongitudeRecordView.as_view(), name='LatitudeLongitude'),
    path('set-last-donated-date/', SetLastDonatedDateRecordView.as_view(), name='LastDonatedDate'),
    path('set-picture/', SetPictureRecordView.as_view(), name='LastDonatedDate'),    
]