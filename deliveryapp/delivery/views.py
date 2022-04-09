from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer, OrderListSerializer, ProductSerializer, CategorySerializer
from .models import User, OrderList, Product, Category


class UserViewSet(viewsets.ViewSet, generics.ListCreateAPIView, generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer

    def get_queryset(self):
        q = self.queryset
        kw = self.request.query_params.get('kw')
        if kw:
            q = q.filter(name__icontains=kw)

        return q


class OrderListViewSet(viewsets.ModelViewSet):
    queryset = OrderList.objects.filter(active=True)
    serializer_class = OrderListSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #
    #     return [permissions.IsAuthenticated()]
    @swagger_auto_schema(
        operation_description='Get the products of a order list',
        responses={
            status.HTTP_200_OK:ProductSerializer()
        }
    )
    @action(methods=['get'], detail=True, url_path='products')
    def get_product(self, request, pk):
        # orderList = OrderList.objects.get(pk=pk)
        orderList = self.get_object()
        products = orderList.products.filter(active=True)
        kw = request.query_params.get('kw')
        if kw:
            products = products.filter(name__icontains=kw)

        return Response(data=ProductSerializer(products, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializer

    # an san phẩm voi product có active =False

    @swagger_auto_schema(
        operation_description="API hide product",
        responses={
            status.HTTP_200_OK: ProductSerializer()
        }
    )
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
