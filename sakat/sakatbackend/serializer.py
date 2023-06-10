from rest_framework import serializers
from .models import User,Doctor,Programs,Program_image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class DoctorSerializer(serializers.ModelSerializer):
    doctor = UserSerializer()
    class Meta:
        model = Doctor
        fields = '__all__'        