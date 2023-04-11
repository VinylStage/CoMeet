from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, nickname,password=None):
        if not nickname:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            nickname=nickname,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname,password=None):
        user = self.create_user(
            nickname=nickname,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        
        
class UserModel(AbstractBaseUser):
    nickname = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

    objects = CustomUserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['name']