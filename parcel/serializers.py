from rest_framework import serializers
from .models import Parcel, ParcelType


class ParcelSerializer(serializers.ModelSerializer):

    delivery_cost = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)
    user = serializers.ReadOnlyField()

    class Meta:
        model = Parcel
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['delivery_cost']:
            data['delivery_cost'] = "Не рассчитано"
        return data


class ParcelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelType
        fields = [
            'id',
            'type'
        ]