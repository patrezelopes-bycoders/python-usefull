import asyncio
from datetime import datetime, timedelta

from asgiref.sync import sync_to_async, async_to_sync
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from . import async_serializer
from .models import Purchase, Sale, Product
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PurchaseSerializer, SaleSerializer
from .utils import discount


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('-date')
    serializer_class = PurchaseSerializer
    permission_classes = []


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer
    permission_classes = []


class SyncAsync(ViewSet):
    authentication_classes = []
    permission_classes = []

    @async_to_sync
    async def async_to_sync_discount(self):
        sale, purchase = await async_serializer.async_discount()
        return sale, purchase

    def async_get(self, request):
        star_time = datetime.now().timestamp()
        sale, purchase = self.async_to_sync_discount()
        response_time = datetime.now().timestamp() - star_time
        return Response(dict(sale=sale, purchase=purchase, time=response_time))

    def sync_get(self, request):
        star_time = datetime.now().timestamp()
        product = Product.objects.all().order_by('?')[0]
        sales = Sale.objects.filter(product=product)
        purchases = Purchase.objects.filter(product=product)
        sales, purchases = discount(sales, purchases)
        response_time = datetime.now().timestamp() - star_time
        return Response(dict(sale=sales, purchase=purchases, time=response_time))
