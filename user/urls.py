from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('user/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/', UserList.as_view(), name = 'userList'),
    path('reg/', RegistrationAPIView.as_view(), name = 'userList'),
    path('login/', LoginAPIView.as_view()),
    path('roles/', RoleList.as_view()),
    path('roles/<int:pk>/', RoleDetails.as_view()),
    path('changepassword/', ChangePasswordView.as_view()),
]