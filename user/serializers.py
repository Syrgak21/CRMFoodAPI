from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Role, User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)
    refresh = self.get_token(self.user)
    data['refresh'] = str(refresh)
    data['access'] = str(refresh.access_token)
    data['roleid'] = self.user.roleid.id
    return data


class RoleSerializer(serializers.ModelSerializer):

  class Meta:
    model = Role
    fields = ['id', 'name']


class RegistrationSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    max_length=50,
    min_length=5,
    write_only=True
  )

  token = serializers.CharField(max_length=255, read_only=True)

  class Meta:
    model = User
    fields = ['name', 'surname', 'username', 'password', 'email', 'roleid', 'dateofadd', 'phone', 'token']

  def create(self, validated_data):
    return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
  username = serializers.CharField(max_length=255, write_only=True)
  password = serializers.CharField(max_length=128, write_only=True, style = {'input_type': 'password'})
  roleid = serializers.IntegerField(source='roleid.id', read_only=True)
  token = serializers.CharField(max_length=255, read_only=True)

  class Meta:
    model = User
    fields = ['username', 'password', 'roleid', 'token']

  def validate(self, data):
    username = data.get('username', None)
    password = data.get('password', None)
      
    if username is None:
      raise serializers.ValidationError('A username is required to log in.')

    if password is None:
      raise serializers.ValidationError('A password is required to log in.')

    user = authenticate(username=username, password=password)

    if user is None:
      raise serializers.ValidationError('A user with this email and password was not found.')

    if not user.is_active:
      raise serializers.ValidationError('This user has been deactivated.')

    return {
      'roleid': user.roleid,
      'token': user.token
    }


class ChangePasswordSerializer(serializers.Serializer):
  oldpassword = serializers.CharField(max_length=255)
  newpassword = serializers.CharField(max_length=128)
  class Meta:
    model = User
    fields = ('oldpassword', 'newpassword')


class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    max_length=50,
    min_length=5,
    write_only=True
  )

  class Meta:
    model = User
    fields = ('id', 'name', 'surname', 'username', 'password', 'email', 'roleid', 'dateofadd', 'phone', 'token',)
    read_only_fields = ('token',)

    def update(self, instance, validated_data):
      password = validated_data.pop('password', None)

      for (key, value) in validated_data.items():
        setattr(instance, key, value)

      if password is not None:
        instance.set_password(password)
      instance.save()
      return instance