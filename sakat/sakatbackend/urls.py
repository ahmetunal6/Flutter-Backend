from django.urls import path
from .views import UserList,CreateUser,DoctorApiView,DoctorListApiView

urlpatterns = [
    path("", UserList.as_view(), name='user_list'),
    path("create", CreateUser.as_view(), name='user_create'),
    path("doctor", DoctorApiView.as_view(), name='user_create'),
    path("doctor_list", DoctorListApiView.as_view(), name='user_create'),   
]