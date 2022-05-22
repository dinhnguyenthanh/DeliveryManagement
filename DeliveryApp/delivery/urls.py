from django.urls import path, include
from . import views
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register(prefix='categories', viewset=views.CategoryViewSet, basename='category')
router.register(prefix='categoryitems', viewset=views.CategoryItemViewSet, basename='categoryitem')
router.register(prefix='goodss', viewset=views.GoodsViewSet, basename='goods')

urlpatterns = [
    path('', include(router.urls)),
]
