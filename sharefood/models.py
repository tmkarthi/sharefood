from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FoodDonation(models.Model):
    AVAILABLE = 'A'
    RESERVED = 'R'
    DELIVERED = 'D'
    STATUS_CHOISES = (
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved'),
        (DELIVERED, 'Delivered')
    )
    donor = models.ForeignKey(User, related_name='donor_set')
    beneficiary = models.ForeignKey(User, related_name='beneficiary_set')
    quantity = models.IntegerField()
    pub_date = models.DateTimeField(verbose_name='date published', auto_now_add=True)
    reserved_date = models.DateTimeField(verbose_name='date reserved')
    delivered_date = models.DateTimeField(verbose_name='date delivered')
    pickup_address = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOISES, default=AVAILABLE)

