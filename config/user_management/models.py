from django.db import models

# Create your models here.

class user(models.Model):
    Username = models.CharField(max_length = 200),
    Password = models.CharField(max_length = 24)

    def __str__(self):
        return self.username



    