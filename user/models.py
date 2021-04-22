from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
  AbstractBaseUser, BaseUserManager, PermissionsMixin
)

import jwt

from datetime import datetime, timedelta


class Role(models.Model):
  name = models.CharField(max_length=20, unique=True)

  def __str__(self):
      return self.name
  

class UserManager(BaseUserManager):
  def create_user(self, name, surname, username, email, roleid, phone, password=None):
    if name is None:
      raise TypeError('User must have a name!')

    if surname is None:
      raise TypeError('User must have a surname!')

    if username is None:
      raise TypeError('User must have a username!')

    if email is None:
      raise TypeError('User must have a email!')

    if phone is None:
      raise TypeError('User must have a phone number!')

    user = self.model(name=name, surname=surname, username=username, email=self.normalize_email(email), roleid=roleid, phone=phone)
    user.set_password(password)
    user.save()

    return user

  def create_superuser(self, name, surname, username, email, roleid, phone, password):
    admin_role = Role.objects.get(pk=roleid)

    if username is None:
      raise TypeError('Superuser must have a username!')

    if password is None:
      raise TypeError('Superuser must have a password!')

    user = self.create_user(
      name = name,
      surname = surname,
      username = username,
      email = self.normalize_email(email),
      roleid = admin_role,
      phone = phone,
      password = password
    )

    user.is_superuser = True
    user.is_staff = True
    user.save()

    return user


class User(AbstractBaseUser, PermissionsMixin):
  name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)
  username = models.CharField(max_length=30, db_index=True, unique=True)
  email = models.EmailField(unique=True)
  roleid = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
  phone = models.CharField(max_length=15)

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  dateofadd = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['name', 'surname', 'email', 'roleid', 'phone']

  objects = UserManager()

  @property
  def token(self):
    return self._generate_jwt_token()

  def _generate_jwt_token(self):
    dt = datetime.now() + timedelta(days=60)
    token = jwt.encode({
      'id': self.pk,
      'exp': dt.utcfromtimestamp(dt.timestamp())
    }, settings.SECRET_KEY, algorithm='HS256')
    return token
