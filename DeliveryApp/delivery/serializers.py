from rest_framework.serializers import ModelSerializer
from .models import Shipper, Customer, Order


class ShipperSerializer(ModelSerializer):
    class Meta:
        model = Shipper
        fields = "__all__"
