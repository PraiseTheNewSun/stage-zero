from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=300)
    stack = models.CharField(max_length=300)

    def __str__(self):
        return self.email