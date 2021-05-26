from django.shortcuts import render
from .sms import send_sms
from .serializers import UserSerializer, BloodSerializer, RegisterSerializer, DonationSerializer, EventSerializer,BloodValidatorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from WebApp.models import Blood
from WebApp.models import Register
from WebApp.models import Donation
from WebApp.models import Event
from WebApp.models import BloodValidator
# import base64
import io
from base64 import decodebytes
# from base64 import decodestring
from django.core.files import File
from django.db.models import Q
from datetime import date

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    # permission_classes = [IsAdminUser]
    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(raise_exception = ValueError):
            serializer.create(validated_data = request.data)
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            
            status=status.HTTP_400_BAD_REQUEST
            
        )

class EventRecordView(APIView):
    def get(self, request):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
        serializer=EventSerializer(data = request.data)
        if serializer.is_valid(raise_exception = ValueError):
            serializer.create(validated_data = request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class RegisterRecordView(APIView):
    def get(self, request):
        register = Register.objects.get( register_id = request.user.id) #filter 
        serializer = RegisterSerializer(register)
        return Response(serializer.data)

    def post(self, request):
        # print(request.data)
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        name = request.data['name']
        gender = request.data['gender']
        number = request.data['number']
        blood_group = request.data['bloodGroup']
        address = request.data['address']
        print("heere")
        # print(request.data['image'])
        if request.data['image'] is not None:
            image_data = bytes(request.data['image'], 'UTF-8')
            image_in_string = decodebytes(image_data)
            image_file = io.BytesIO(image_in_string)
        # print(image_file)
        if User.objects.filter(username = username).exists():

            return Response(
            {
                "error": True,
                "error_msg": "Username already exists",
            },

            status=status.HTTP_400_BAD_REQUEST
        )
        if User.objects.filter(email=email).exists():
                return Response(
                {
                    "error": True,
                    "error_msg": "Email already exists",
                },
                status=status.HTTP_400_BAD_REQUEST
        )

        user=User.objects.create_user(username = username, password = password, email = email)
        
        user.set_password(password)
        register=Register.objects.create(register_id = user, name = name, gender = gender, address = address, number = number, blood_group = blood_group)
        
        if register is not None:
            if request.data['image'] is not None:
                register.image.save(f'{username}.png', File(image_file))
                register.save()
            user.save()
            print("Success")
            return Response(
                {
                "scuccess": True,
                "success_msg": "Successfully created",
            },
                status=status.HTTP_201_CREATED
            )
        else:
            User.objects.filter(username = username).delete()
            return Response(
            {
                "error": True,
                "error_msg": "Error",
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        pass
        serializer=RegisterSerializer(data = request.data)
        if serializer.is_valid(raise_exception = ValueError):
            serializer.create(validated_data = request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class DonationRecordView(APIView):
    def get(self, request):
        register = Register.objects.get(register_id=request.user.id)
        print(register)
        donation = Donation.objects.filter(donor_id = register)
        serializer = DonationSerializer(donation, many=True)
        return Response(serializer.data)
    def post(self,request):
        donor_id = request.data['donor_id']
        request_id = request.data['request_id']
        blood = Blood.objects.get(request_id=request_id)
        user = Register.objects.get(register_id=donor_id)
        # status = request.data['status']
        if Donation.objects.filter(request_id=blood, donor_id=user, date=date.today()).exists():
            return Response({
                'error': True,
                'error_msg': 'Cannot process at this moment'
            }, status=status.HTTP_400_BAD_REQUEST,)
        donate = Donation.objects.create(request_id=blood, donor_id=user, status=False)
        if donate is None:
            return Response({
                'error': True,
                'error_msg': 'You have already donated'
            }, status=status.HTTP_400_BAD_REQUEST,)
        blood.status = True
        user.available_status = False
        blood.save()
        return Response({
            'success': True,
            'success_msg': 'Successfully Created'
        }, status=status.HTTP_200_OK,)
        pass
        serializer=DonationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class SetLatitudeLongitudeRecordView(APIView):
    def post(self, request):
        try:
            latitude = request.data['latitude']
            longitude = request.data['longitude']
            user = Register.objects.get(register_id=request.user.id)
            user.latitude = latitude
            user.longitude = longitude
            user.save()
            return Response(
                {
                    'success': True,
                    'success_msg': 'Successfully changed',
            }, status=status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    'error': True,
                    'error_msg': 'Cannot perform the request at the moment',
            }, status=status.HTTP_400_BAD_REQUEST
            )

class SetAvailabilityRecordView(APIView):
    def post(self, request):
        try:
            available_status = request.data['status']
            user = Register.objects.get(register_id=request.user.id)
            user.available_status = available_status
            user.save()
            return Response(
                {
                    'success': True,
                    'success_msg': 'Successfully changed',
            }, status=status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    'error': True,
                    'error_msg': 'Cannot perform the request at the moment',
            }, status=status.HTTP_400_BAD_REQUEST
            )
        
class SetLastDonatedDateRecordView(APIView):
    def post(self, request):
        try:
            available_date= request.data['date']
            user = Register.objects.get(register_id=request.user.id)
            print(available_date)
            user.last_donated_date = available_date
            user.save()
            return Response(
                {
                    'success': True,
                    'success_msg': 'Successfully changed',
            }, status=status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    'error': True,
                    'error_msg': 'Cannot perform the request at the moment',
            }, status=status.HTTP_400_BAD_REQUEST
            )

class SetPictureRecordView(APIView):
    def post(self, request):
        try:
            image_data = bytes(request.data['image'], 'UTF-8')
            image_in_string = decodebytes(image_data)
            image_file = io.BytesIO(image_in_string)
            user = Register.objects.get(register_id=request.user.id)
            user.image.save(f'{user.number}.png', File(image_file))
            user.save()
            return Response(
                {
                    'success': True,
                    'success_msg': 'Successfully changed',
            }, status=status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    'error': True,
                    'error_msg': 'Cannot perform the request at the moment',
            }, status=status.HTTP_400_BAD_REQUEST
            )

class BloodValidatorRecordView(APIView):
    def get(self, request):
        BloodValidator = BloodValidator.objects.all()
        serializer = BloodValidatorSerializer(BloodValidator, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
        serializer = BloodValidatorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
class BloodRecordView(APIView):
    def get(self, request):
        print(request.user.id)
        register = Register.objects.get(register_id = request.user.id)
        print(register)
        blood = Blood.objects.exclude(register_id=register)
        print(blood)
        filtered_blood = blood.filter(status=False, blood_group=register.blood_group)
        print(blood)

        serializer = BloodSerializer(filtered_blood, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_id = request.data['register_id']
        user = None
        if request_id is not None:
            user = Register.objects.get(register_id=request.user.id)
        request_id = request.data['request_id']
        patient_name = request.data['patient_name']
        blood_group = request.data['blood_group']
        gender = request.data['gender']
        number = request.data['number']
        case = request.data['case']
        hospital = request.data['hospital']
        required_date = request.data['required_date']
        print(request_id)
        validate_blood = None
        if BloodValidator.objects.filter(request_id = request_id).exists():
            validate_blood = BloodValidator.objects.get(request_id=request_id)       
        else:
            return Response(
            {
                "error": True,
                "error_msg": "Request ID not found",
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        
        if Blood.objects.filter(request_id=validate_blood).exists():
            return Response(
            {
                "error": True,
                "error_msg": "Request already exists",
            },
            status=status.HTTP_400_BAD_REQUEST
        )        
        
        list_of_donors = Register.objects.exclude(register_id= request.user.id)
        filtered_list_of_donors = list_of_donors.filter(blood_group = blood_group, is_verified = True)
        numbers_text = ''
        for donor in filtered_list_of_donors:
            numbers_text = numbers_text + str(donor.number) + ','
        print(numbers_text)

        if user is not None:
            blood=Blood.objects.create(request_id=validate_blood, register_id=user, patient_name = patient_name, blood_group = blood_group, gender = gender, number = number, case = case, hospital = hospital, required_date = required_date)
            if blood is not None:
                print("Success")
                print(send_sms(numbers_text, patient_name, blood_group, case, hospital, required_date, number))
                return Response(
                    {
                    "success": True,
                    "success_msg": "Request recorded",
                },
                    status=status.HTTP_201_CREATED
                )
        blood=Blood.objects.create(request_id=validate_blood, patient_name = patient_name, blood_group = blood_group, gender = gender, number = number, case = case, hospital = hospital, required_date = required_date)
        if blood is not None:
            print("Success")
            print(send_sms(numbers_text, patient_name, blood_group, case, hospital, required_date, number))
            return Response(
                {
                "success": True,
                "success_msg": "Request recorded",
            },
                status=status.HTTP_201_CREATED
            )
            
        pass
        try:
            print("HI")
        except:
            return Response(
                {
                "error": True,
                "error_msg": "Cannot perform the task at the moment",
            },
                status=status.HTTP_400_BAD_REQUEST
            )

class ListDonorRecord(APIView):
    def get(self, request, blood_group):
        list_of_donors = Register.objects.exclude(register_id= request.user.id)
        filtered_list_of_donors = list_of_donors.filter(blood_group = blood_group, is_verified = True)
        serializer = RegisterSerializer(filtered_list_of_donors, many=True)

        return Response(serializer.data)



