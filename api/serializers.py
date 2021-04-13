from django.contrib.auth.models import User
# from WebApp.models import Register
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from WebApp.models import Register, Blood


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

class BloodSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        blood = Blood.objects.create_user(**validated_data)
        return blood

    class Meta:
        model = Blood
        fields = '__all__'
        depth = 1
        # 'patientName',
            # 'bloodGroup',
            # 'gender',
            # 'number',
            # 'requiredDate',
            # 'case'
            # 'hospital'
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset = Blood.objects.all(),
        #         fields=['number']
        #     )
        # ]