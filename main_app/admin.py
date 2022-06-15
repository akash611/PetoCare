from django.contrib import admin

# Register your models here.
from main_app.models import  Provider, Vet, Training, Grooming, VetBooking, TrainingBooking, GroomingBooking

# admin.site.register(User)
admin.site.register(Provider)
admin.site.register(Vet)
admin.site.register(Training)
admin.site.register(Grooming)
admin.site.register(VetBooking)
admin.site.register(TrainingBooking)
admin.site.register(GroomingBooking)