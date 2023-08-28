from rest_framework.routers import DefaultRouter
from .views import ParcelViewSet, ParcelTypeViewSet


router = DefaultRouter()
router.register(r'parcels', ParcelViewSet)
router.register(r'parcel_types', ParcelTypeViewSet)
urlpatterns = router.urls