from django.db import models

pr_status = (("Not Verified","Not Verified"), ("Verified","Verified"), ("Inactive","Inactive"))
ap_status = (("Registered","Registered"), ("Confirmed","Confirmed"), ("Fullfilled","Fullfilled"))

# Create your models here.


class Petparent(models.Model):
    pp_id = models.IntegerField( primary_key="True")
    name = models.CharField(max_length=70)
    email_id = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.CharField(max_length=6)


class Groomer(models.Model):
    groomer_id = models.IntegerField(primary_key="True")
    name = models.CharField(max_length=70)
    email_id = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.CharField(max_length=6)
    status = models.CharField(max_length=100, choices=pr_status, default="Not Verified")


class Vet(models.Model):
    vet_id = models.IntegerField(primary_key="True")
    name = models.CharField(max_length=70)
    email_id = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.CharField(max_length=6)
    status = models.CharField(max_length=20, choices=pr_status, default="Not Verified")
    fees = models.IntegerField()


class Services(models.Model):
    service_id = models.IntegerField(primary_key="True")
    service_type = models.CharField(max_length=20)
    service_name = models.CharField(max_length=20, default="")
    service_desc = models.CharField(max_length=100)
    fees = models.IntegerField()


class VetBooking(models.Model):
    booking_id = models.IntegerField(primary_key="True")
    pp_id = models.ForeignKey(Petparent,on_delete=models.CASCADE)
    vet_id = models.ForeignKey(Vet,on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50)
    illness_details = models.CharField(max_length=100)
    appo_date_time = models.DateTimeField()
    appo_full_date_time = models.DateTimeField()
    appo_status = models.CharField(max_length=15)

class ServiceBooking(models.Model):
    booking_id = models.IntegerField(primary_key="True")
    pp_id = models.ForeignKey(Petparent,on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    groomer_id = models.ForeignKey(Groomer,on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50)
    illness_details = models.CharField(max_length=100)
    appo_date_time = models.DateTimeField()
    appo_full_date_time = models.DateTimeField()
    appo_status = models.CharField(max_length=15)