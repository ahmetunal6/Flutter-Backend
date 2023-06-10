from django.shortcuts import render
from rest_framework import generics
from account.serializer import UserSerializer,UpdateUserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import filters
class CreateUserApiView(generics.CreateAPIView):
    
##
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        return Response(serializer.validated_data, status=201,)
    



class ListUsersApiView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class LoginApiView(generics.GenericAPIView):
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            token_value = token.key 
            id=str(request.user.id)
            return Response({"message": "giriş başarılı","token": token_value,'id':id}, status=status.HTTP_200_OK)
    
        else:
            return Response({"message": "Kullanıcı adı veya şifre yanlış."}, status=status.HTTP_401_UNAUTHORIZED)
# class LogoutApiView(generics.GenericAPIView):

#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         # Logout the user
#         logout(request)
#         # Return success response
#         return Response({"message": "Başarıyla çıkış yapıldı."})
from rest_framework.views import APIView
class LogoutApiView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        # Token'i geçerli kullanıcıya ait olanı al
        token = request.auth
        if token:
            # Token'i geçersizleştir
            token.delete()
            return Response({"message": "Başarıyla çıkış yapıldı."}, status=200)
        else:
            return Response({"message": "Token bulunamadı."}, status=400)
        
class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = "id"
    

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset       
        

