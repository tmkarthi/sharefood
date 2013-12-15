from rest_framework import serializers
from sharefood.models import DonatedFood
from django.contrib.auth.models import User


class DonatedFoodSerializer(serializers.HyperlinkedModelSerializer):
    donor_name = serializers.Field(source='donor.username')

    class Meta:
        model = DonatedFood


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'donated_food_set')