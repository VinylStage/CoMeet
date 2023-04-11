from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class UserModel(AbstractBaseUser):
    class Meta:
        db_table = "my_user"
