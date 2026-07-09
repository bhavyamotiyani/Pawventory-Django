from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=10, unique=True)
    dob = models.DateField()
    pwd = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name
