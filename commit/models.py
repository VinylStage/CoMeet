# tweet/models.py
from django.db import models
from user.models import models


# Create your models here.
class Commit(models.Model):
    class Meta:
        db_table = "commit"

    author = models.ForeignKey(models, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
