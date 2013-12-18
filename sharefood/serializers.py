from rest_framework import serializers
from sharefood.models import DonatedFood, FoodReservation
from django.contrib.auth.models import User


class DonatedFoodSerializer(serializers.ModelSerializer):
    donor = serializers.Field(source='donor.username')
    pub_date = serializers.Field(source='pub_date')
    status = serializers.Field(source='status')

    class Meta:
        model = DonatedFood
        fields = ('id', 'donor', 'description', 'quantity', 'pub_date', 'pickup_address', 'status')


class FoodReservationSerializer(serializers.ModelSerializer):
    donation = serializers.Field(source='donation.id')
    beneficiary = serializers.Field(source='beneficiary.username')
    reserved_date = serializers.Field(source='reserved_date')
    delivered_date = serializers.Field(source='delivered_date')
    status = serializers.Field(source='status')

    class Meta:
        model = FoodReservation
        fields = (
            'id', 'donation', 'beneficiary', 'description', 'quantity', 'reserved_date', 'delivered_date', 'status')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'donated_food_set')