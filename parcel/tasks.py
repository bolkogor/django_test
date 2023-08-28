from decimal import Decimal as D
import django
django.setup()
from .models import Parcel
from dj_test.celery import app


@app.task
def calculate_delivery_cost():
    parcels_to_update = list(Parcel.objects.filter(delivery_cost=None))
    for parcel in parcels_to_update:
        parcel.delivery_cost = parcel.weight * D(0.5) * parcel.value * D(0.01) * 95  # todo: cache in redis
    Parcel.objects.bulk_update(parcels_to_update, ['delivery_cost'])

    return f'{len(parcels_to_update)} delivery cost calculated'
