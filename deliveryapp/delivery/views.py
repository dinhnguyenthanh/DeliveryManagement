from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import OrderList
from .serializers import OrderListSerializer


class OrderListViewSet(viewsets.ModelViewSet):
    queryset = OrderList.objects.filter(active=True)
    serializer_class = OrderListSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]

    # list(get) --> xem danh sach cac san pham
    # detail --> xem chi tiet 1 san pham
    # (post) --> them san pham
    #   (delete) --> xoa san pham
    #   (put) --> cap nhat


def home(request):
    return HttpResponse("Hello")
