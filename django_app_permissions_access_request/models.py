from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.CharField(max_length=5000, default="")
    timestamp = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = [['user', 'group']]



    


