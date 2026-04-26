from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices


# Manager Class for CustomUser Model
# where createsuperuser command can be edited
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a User with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)

        extra_fields.setdefault("username", email) # makes the username the email

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("username", email) # resolves issure with username field

        return self.create_user(email, password, **extra_fields)

# Create your models here.
class CustomUser(AbstractUser):
    is_organization = models.BooleanField(default=False)
    is_contributor = models.BooleanField(default=False)
    is_recipient = models.BooleanField(default=False)

    email = models.EmailField(unique=True) # email is unique identifier
    username = models.CharField(max_length=150, blank=True, null=True, unique=False) # not required

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager() # attaches manager class to model

    def __str__(self):
        return self.email

class Organization(models.Model):
    # who creates the organization profile?? aka who owns it??
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organization')
    name = models.CharField(max_length=255, null=False, blank=False)
    size = models.IntegerField()
    industry = models.CharField(max_length=150)

class Contributor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='contributor_profile')
    first_name = models.CharField(max_length=150, blank=False) # required in forms
    last_name = models.CharField(max_length=150, blank=False) # reuired in forns
    # email tied to CustomUser model
    is_employer = models.BooleanField(default=False)
    max_num_containers = models.IntegerField(default=10) # default can be changed with a subscription?
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='contributors') # required by default

class Recipient(models.Model):
    STATUS = Choices('is_active', 'is_inactive')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='recipient_profile')
    first_name = models.CharField(max_length=150, blank=False) # required in forms
    last_name = models.CharField(max_length=150, blank=False) # reuired in forns
    # email tied to CustomUser model
    status = StatusField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='recipients')
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, related_name='supervising_contributor')