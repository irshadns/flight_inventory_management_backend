from django.contrib import admin
from .models import User, Flight, Airport

# admin.site.register(User)
# admin.site.register(Flight)
# admin.site.register(Airport)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['origin', 'destination', 'flight_number', 'departure_date_time', 'arrival_date_time', 'base_fare', 'tax']

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ['iata_code', 'city']

