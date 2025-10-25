from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name