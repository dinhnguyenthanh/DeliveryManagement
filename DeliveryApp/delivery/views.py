from rest_framework import viewsets, generics
from .models import Shipper, Customer, Order
from .serializers import ShipperSerializer


class ShipperViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Shipper
    serializer_class = ShipperSerializer

