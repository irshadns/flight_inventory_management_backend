from rest_framework import serializers
from .models import User, Flight, Airport

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)     
        instance.save()
        return instance

class FlightPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('origin', 'destination', 'flight_number', 'departure_date_time', 'arrival_date_time')
        # fields = '__all__'

class FlightAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'