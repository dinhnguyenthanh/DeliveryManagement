from django.urls import include, path, re_path
from . import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orderLists', views.OrderListViewSet)
router.register('products', views.ProductViewSet)
router.register('users', views.UserViewSet)

# /delivery/ - get
# /delivery/ - post
# /delivery/{orderList_id}/ - get
# /delivery/{orderList_id}/ - put
# /delivery/{orderList_id}/ - delete
urlpatterns = [
    path('', include(router.urls))
]
