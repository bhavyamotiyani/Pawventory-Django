from django.db import models

# Class = Tables
# Variables = Columns
# ~Objects = Rows

class user(models.Model):

    name = models.CharField(max_length=255)
    email = models.TextField(max_length=250)
    contact_no = models.CharField(max_length=15, unique=True)
    dob = models.DateField()
    pwd = models.CharField(max_length=266)
    c_pwd = models.CharField(max_length=266)
    gender = models.CharField(max_length=255)

