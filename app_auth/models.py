from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Department Name')
    class Meta:
        db_table            = "app_auth_department"
        verbose_name        = 'Department'
        verbose_name_plural = '01 - Departments'
    def __str__(self):
        return self.name
    
class Title(models.Model):
    name = models.CharField(max_length=150, verbose_name="Title Name")
    class Meta:
        db_table            = "app_auth_title"
        verbose_name        = 'Title'
        verbose_name_plural = '02 - Titles'
    def __str__(self):
        return self.name
    

class AccountManager(BaseUserManager):
    def create_user(self, email, full_name, password):
        if not email:
            raise ValueError("Email address is required")
        if not full_name:
            raise ValueError("Full name is required.")
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=50, verbose_name="Full Name")
    photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True, verbose_name="Profile Photo")
    department = models.ForeignKey(Department, verbose_name="Department", null=True, blank=True, on_delete=models.RESTRICT)
    title = models.ForeignKey(Title, verbose_name="Title", null=True, blank=True, on_delete=models.RESTRICT)
    phone_gsm = models.CharField(max_length=12, verbose_name="Mobile Number", null=True, blank=True)
    phone_internal = models.CharField(max_length=5, verbose_name="Internal Phone", null=True, blank=True)
    date_joined = models.DateField(auto_now=True, verbose_name="Join Date", null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = AccountManager()
    
    class Meta:
        db_table = "app_auth_accounts"
        verbose_name = "User"
        verbose_name_plural = "03 - Users"
    def __str__(self) -> str:
        return self.full_name