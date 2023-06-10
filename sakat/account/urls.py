from django.urls import path
from .views import CreateUserApiView,ListUsersApiView,LoginApiView,LogoutApiView,UserDetailApiView

urlpatterns = [
    path("", ListUsersApiView.as_view(), name='user_create'),
    path("create", CreateUserApiView.as_view(), name='user_create'),
    path("login/<int:id>", UserDetailApiView.as_view(), name='user_create'),
    path("login", LoginApiView.as_view(), name='user_create'),
    path("logout", LogoutApiView.as_view(), name='user_create'),
]