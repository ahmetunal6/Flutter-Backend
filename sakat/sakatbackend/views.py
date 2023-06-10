from rest_framework import generics
from .serializer import UserSerializer,DoctorSerializer
from .models import User,Doctor

class UserList(generics.ListAPIView):
    
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class DoctorApiView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class DoctorListApiView(generics.ListAPIView):
    
    serializer_class = DoctorSerializer
    def get_queryset(self):
        queryset = Doctor.objects.all()
        return queryset
          
