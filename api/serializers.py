from django.contrib.auth.models import User
# from WebApp.models import Register
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from WebApp.models import Register, Blood, Donation, Event, BloodValidator


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        register = Register.objects.create_user(**validated_data)
        return user, register

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]
class EventSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        event = Event.objects.create_user(**validated_data)
        return event
    class Meta:
        model=Event
        fields = '__all__'
        depth = 1

class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        register = Register.objects.create_user(**validated_data)
        return blood
    class Meta:
        model=Register
        fields = '__all__'
        depth = 1

class DonationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        donation =  Donation.objects.create_user(**validated_data)
        return donation
    class Meta:
        model = Donation
        fields = '__all__'
        depth = 1

class BloodValidatorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        BloodValidator = BloodValidator.objects.create_user(**validated_data)
        return BloodValidator
    class Meta:
        model=BloodValidator
        fields = '__all__'
        depth = 1

class BloodSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        blood = Blood.objects.create_user(**validated_data)
        return blood

    class Meta:
        model = Blood
        fields = '__all__'
        depth = 1
       