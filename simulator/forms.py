from django import forms

from simulator.models import Airport, Flight

class AirportForm(forms.Form):
    class meta:
        model = Airport
        fields = ['name', 'code', 'city', 'country'] #good for code practice, but not necessary for this form
        # fields = '__all__'  #it gather all files of the model, but not necessary for this form

class FlightForm(forms.Form):
    class meta:
        model = Flight
        fields = ['flight_number', 'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time']

