from django.contrib import admin
from simulator.models import Airport, Flight


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "city", "country")
    search_fields = ("name", "code", "city", "country")


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "flight_number",
        "departure_airport",
        "arrival_airport",
        "departure_time",
        "arrival_time",
        "created_by",
        "created_at",
    )

    search_fields = (
        "flight_number",
        "departure_airport__name",
        "arrival_airport__name",
    )

    list_filter = (
        "departure_airport",
        "arrival_airport",
        "departure_time",
    )