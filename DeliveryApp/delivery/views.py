from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, CategoryItem, Goods
from .serializer import CategorySerializer, CategoryItemSerializer, GoodsSerializer
from drf_yasg.utils import swagger_auto_schema
from .paginators import CategoryItemPaginator


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = self.queryset
        kw = self.request.query_params.get("kw")
        if kw:
            q = q.filter(name__icontains=kw)

        return q


class CategoryItemViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = CategoryItem.objects.filter(active=True)
    serializer_class = CategoryItemSerializer
    pagination_class = CategoryItemPaginator

    def get_queryset(self):
        queryset = self.queryset
        kw = self.request.query_params.get("kw")
        if kw:
            queryset = queryset.filter(name__icontains=kw)

        category_id = self.request.query_params.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    @swagger_auto_schema(
        operation_description='Get the goods of a category item',
        responses={
            status.HTTP_200_OK: GoodsSerializer()
        }
    )
    @action(methods=['get'], detail=True, url_path='goodss')
    def get_goodss(self, request, pk):
        categoryitem = self.get_object()
        goodss = categoryitem.goodss.filter(active=True)

        kw = request.query_params.get("kw")
        if kw:
            goodss = goodss.filter(name__icontains=kw)

        return Response(data=GoodsSerializer(goodss, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class GoodsViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Goods.objects.filter(active=True)
    serializer_class = GoodsSerializer

