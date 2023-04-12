from django.db import models
from user.models import User


# Create your models here.
class Commit(models.Model):
    class Meta:
        db_table = "my_commit"

    title = models.CharField(max_length=256, default='')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    class Meta:
        db_table = "comment"
        
    commit = models.ForeignKey(Commit, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)