from django.urls import path
from .views import UserRecordView, BloodRecordView


app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('blood/', BloodRecordView.as_view(), name='blood'),
]