from rest_framework.viewsets import ModelViewSet
from .serializers import ParcelSerializer, ParcelTypeSerializer
from .models import Parcel, ParcelType





class ParcelViewSet(ModelViewSet):
    serializer_class = ParcelSerializer
    queryset = Parcel.objects.all()
    
    def create(self, request, *args, **kwargs):
        return super(ParcelViewSet, self).create(request, *args, **kwargs)


class ParcelTypeViewSet(ModelViewSet):
    serializer_class = ParcelTypeSerializer
    queryset = ParcelType.objects.all()
