from django.urls import include, path
from rest_framework import routers
from inventory import views
from inventory.views import SyncAsync

router = routers.DefaultRouter()
router.register(r'purchase', views.PurchaseViewSet, basename='purchase')
router.register(r'sale', views.SaleViewSet, basename='sale')
sync_view = SyncAsync.as_view({"get": "sync_get"})
async_view = SyncAsync.as_view({"get": "async_get"})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('sync_view', sync_view, name='sync_view'),
    path('async_view', async_view, name='async_view'),
]