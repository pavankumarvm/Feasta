from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import FeastaUserManager
from mess.models import Mess

# Create your models here.

STAY_TYPES = (('Hostel','Hostel'), ('Flat','Flat'), ('Localite','Localite'), ('Others','Others'),)
GENDER = (('Male','Male'), ('Female','Female'))

class FeastaUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, blank=False, null=False, unique=True, primary_key=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=True, default="")
    email = models.EmailField(max_length=300, unique=True, blank=False, null=False)
    phone_no = models.CharField(max_length=10, blank=False, null=False)
    profile_photo = models.ImageField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_messowner = models.BooleanField(default=False, blank=False, null=False)
    is_consumer = models.BooleanField(default=False, blank=False, null=False)

    objects = FeastaUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True



class MessOwner(models.Model):
    user = models.OneToOneField(FeastaUser, on_delete=models.CASCADE, primary_key=True)
    # mess_name = models.CharField(max_length=30, blank=True)
    # address = models.CharField(max_length=300, blank=True)

    mess_id = models.ForeignKey(Mess, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return self.mess_id.mess_name

    def get_username(self):
        return self.user.username

    def owner_name(self):
        return (self.user.first_name + ' ' + self.user.last_name)


class Consumer(models.Model):
    user = models.OneToOneField(FeastaUser, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=10, choices=GENDER,default=None)
    college = models.CharField(max_length=200, blank=True)
    stay_type = models.CharField(max_length=20, choices=STAY_TYPES, default='Hostel')

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username
