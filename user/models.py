import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True, blank=True)
    contact_name = models.CharField(max_length=50)
    contact_phone_number = models.CharField(max_length=50)
    create_date_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.code + ' - ' + self.name

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password is not provided')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name, 
            last_name = last_name,
            mobile = mobile,
            **extra_fields 
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email, username, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, first_name, last_name, mobile, **extra_fields)

    def create_superuser(self, email, username, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, username, password, first_name, last_name, mobile, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    username = models.CharField(max_length=255, null=False, unique=True, default='')
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=250)    

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users' 


    