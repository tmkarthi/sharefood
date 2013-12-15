from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DonatedFood(models.Model):
    AVAILABLE = 'A'
    RESERVED = 'R'
    DELIVERED = 'D'
    CANCELLED = 'C'
    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    )
    donor = models.ForeignKey(User, related_name='donated_food_set')
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    pub_date = models.DateTimeField(verbose_name='date published', auto_now_add=True)
    pickup_address = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=AVAILABLE)


class FoodReservation(models.Model):
    RESERVED = 'R'
    DELIVERED = 'D'
    CANCELLED = 'C'
    STATUS_CHOICES = (
        (RESERVED, 'Reserved'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    )
    donation = models.ForeignKey(DonatedFood)
    beneficiary = models.ForeignKey(User, related_name='received_food_set')
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    reserved_date = models.DateTimeField(verbose_name='date reserved', auto_now_add=True)
    delivered_date = models.DateTimeField(verbose_name='date delivered')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=RESERVED)
