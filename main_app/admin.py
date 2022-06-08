from django.contrib import admin

# Register your models here.
from main_app.models import Petparent, Groomer, Vet, Services, VetBooking, ServiceBooking

admin.site.register(Petparent)
admin.site.register(Groomer)
admin.site.register(Vet)
admin.site.register(Services)
admin.site.register(VetBooking)
admin.site.register(ServiceBooking)