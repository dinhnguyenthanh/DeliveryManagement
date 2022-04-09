from django.db import router
from django.urls import include, path, re_path
from . import views
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()
router.register(prefix='users', viewset=views.UserViewSet, basename='user')
router.register(prefix='categories', viewset=views.CategoryViewSet, basename='category')
router.register(prefix='orderLists', viewset=views.OrderListViewSet, basename='orderList')
router.register(prefix='products', viewset=views.ProductViewSet, basename='product')
router.register(prefix='comments', viewset=views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]
