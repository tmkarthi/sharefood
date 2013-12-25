from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DonatedFood(models.Model):
    AVAILABLE = 'A'
    DELIVERED = 'D'
    CANCELLED = 'C'
    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    )
    donor = models.ForeignKey(User, related_name='donated_food_set')
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    pub_date = models.DateTimeField(verbose_name='date published', auto_now_add=True)
    pickup_address_1 = models.CharField(max_length=100)
    pickup_address_2 = models.CharField(max_length=100)
    pickup_city = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=10)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=AVAILABLE)

    @property
    def balance_quantity(self):
        reservations = self.foodreservation_set.exclude(
            status__in=[FoodReservation.CANCELLED, FoodReservation.REQUESTED])
        balance = self.quantity
        for reservation in reservations:
            balance -= reservation.quantity
        return balance


class FoodReservation(models.Model):
    REQUESTED = 'R'
    ACCEPTED = 'A'
    DELIVERED = 'D'
    CANCELLED = 'C'
    RESERVATION_STATUS_CHOICES = (
        (REQUESTED, 'Requested'),
        (ACCEPTED, 'Accepted'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    )
    donation = models.ForeignKey(DonatedFood)
    beneficiary = models.ForeignKey(User, related_name='received_food_set')
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    reserved_date = models.DateTimeField(verbose_name='date reserved', auto_now_add=True)
    delivered_date = models.DateTimeField(verbose_name='date delivered', null=True)
    status = models.CharField(max_length=1, choices=RESERVATION_STATUS_CHOICES, default=REQUESTED)
