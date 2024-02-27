from rest_framework import serializers

from snippets.models import Car, Owner


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    car = CarSerializer()  # Nested serialization of the Car model

    class Meta:
        model = Owner
        fields = '__all__'

    def create(self, validated_data):
        car_data = validated_data.pop('car')  # Extract car data
        car_instance = Car.objects.create(**car_data)  # Create Car instance
        owner_instance = Owner.objects.create(car=car_instance, **validated_data)  # Create Owner instance with Car
        return owner_instance


