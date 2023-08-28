from django.db import models
from django.contrib.auth import get_user_model


user_model = get_user_model()


class ParcelType(models.Model):
    PARCEL_TYPES = (
        ('EL', 'Electronics'),
        ('CL', 'Clothes'),
        ('OT', 'Other')
    )
    type = models.CharField(choices=PARCEL_TYPES, max_length=30)


class Parcel(models.Model):
    name = models.CharField(max_length=200)
    weight = models.DecimalField(decimal_places=2, max_digits=8)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    type = models.ForeignKey(to=ParcelType, on_delete=models.SET_NULL, null=True)
    delivery_cost = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    user = models.ForeignKey(to=user_model, null=True, on_delete=models.CASCADE)
