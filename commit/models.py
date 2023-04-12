from django.db import models
from user.models import User


# Create your models here.
class Commit(models.Model):
    class Meta:
        db_table = "my_commit"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
