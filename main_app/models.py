from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User

pr_status = (("Not Verified", "Not Verified"),
             ("Verified", "Verified"), ("Inactive", "Inactive"))
ap_status = (("Registered", "Registered"), ("Confirmed",
             "Confirmed"), ("Fullfilled", "Fullfilled"))

# Create your models here.


class UserDetails(models.Model):
   user= models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
   phone_number = models.CharField(max_length=10,unique="True")
   address = models.CharField(max_length=100,null="True",blank="True")
   pin = models.CharField(max_length=6,null="True",blank="True")

class Provider(models.Model):
    provider_id = models.IntegerField(primary_key="True")
    name = models.CharField(max_length=70)
    email_id = models.EmailField(max_length=100,unique="True")
    phone_number = models.CharField(max_length=10,unique="True")
    address = models.CharField(max_length=100,null="True",blank="True")
    city = models.CharField(max_length=50,null="True",blank="True")
    pin = models.CharField(max_length=6,null="True",blank="True")
    status = models.CharField(
        max_length=100, choices=pr_status, default="Not Verified")
    image = models.ImageField(upload_to='provider', default="")


class Vet(models.Model):
    vet_id = models.IntegerField(primary_key="True")
    name = models.CharField(max_length=70)
    email_id = models.EmailField(max_length=100,unique="True")
    phone_number = models.CharField(max_length=10,unique="True")
    address = models.CharField(max_length=100,null="True",blank="True")
    city = models.CharField(max_length=50,null="True",blank="True")
    pin = models.CharField(max_length=6,null="True",blank="True")
    status = models.CharField(
        max_length=20, choices=pr_status, default="Not Verified")
    fees = models.IntegerField()
    image = models.ImageField(upload_to='vet', default="")


class Training(models.Model):
    training_id = models.IntegerField(primary_key="True")
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    fees = models.IntegerField()
    image = models.ImageField(upload_to='training', default="")


class Grooming(models.Model):
    grooming_id = models.IntegerField(primary_key="True")
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    fees = models.IntegerField()
    image = models.ImageField(upload_to='grooming', default="")


class VetBooking(models.Model):
    booking_id = models.IntegerField(primary_key="True")
    pp_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vet_id = models.ForeignKey(Vet, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50)
    illness_details = models.CharField(max_length=100)
    appo_date_time = models.DateTimeField()
    appo_full_date_time = models.DateTimeField()
    appo_status = models.CharField(
        max_length=100, choices=ap_status, default="Registered")


class TrainingBooking(models.Model):
    booking_id = models.IntegerField(primary_key="True")
    pp_id = models.ForeignKey(User, on_delete=models.CASCADE)
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50,null="True",blank="True")
    pet_type = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50,null="True",blank="True")
    appo_date_time = models.DateTimeField()
    appo_full_date_time = models.DateTimeField()
    appo_status = models.CharField(
        max_length=100, choices=ap_status, default="Registered")


class GroomingBooking(models.Model):
    booking_id = models.IntegerField(primary_key="True")
    pp_id = models.ForeignKey(User, on_delete=models.CASCADE)
    grooming_id = models.ForeignKey(Grooming, on_delete=models.CASCADE)
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50,null="True",blank="True")
    pet_type = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50,null="True",blank="True")
    appo_date_time = models.DateTimeField()
    appo_full_date_time = models.DateTimeField()
    appo_status = models.CharField(
        max_length=100, choices=ap_status, default="Registered")
