from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import OrderList, Product, User
from .serializers import OrderListSerializer, ProductSerializer, UserSerializer


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]


class OrderListViewSet(viewsets.ModelViewSet):
    queryset = OrderList.objects.filter(active=True)
    serializer_class = OrderListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #
    #     return [permissions.IsAuthenticated()]

    # list(get) --> xem danh sach cac san pham
    # detail --> xem chi tiet 1 san pham
    # (post) --> them san pham
    #   (delete) --> xoa san pham
    #   (put) --> cap nhat


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializer

    # an san phẩm voi product có active =False

    # /product/{pk}/hide-product
    @action(methods=['post'], detail=True, url_path='hide-product', url_name='hide-product')
    def hide_product(self, request, pk):
        try:
            p = Product.objects.get(pk=pk)
            p.active = False
            p.save()
        except Product.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=ProductSerializer(p, context={'request': request}).data, status=status.HTTP_200_OK)
