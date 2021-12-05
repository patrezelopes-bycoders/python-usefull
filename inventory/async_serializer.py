from datetime import datetime
from decimal import Decimal
import concurrent.futures

from django.db.models import F

from inventory.models import Sale, Purchase, Product
import asyncio

from asgiref.sync import sync_to_async
from inventory.utils import get_purchase as _get_purchase
from inventory.utils import get_sale as _get_sale
from inventory.utils import random_product as _random_product


@sync_to_async(thread_sensitive=False)
def async_get_sale(sales):
    return _get_sale(sales)


@sync_to_async(thread_sensitive=False)
def async_get_purchase(purchases):
    return _get_purchase(purchases)


@sync_to_async
def async_get_product():
    return _random_product()


async def async_discount():
    product = await async_get_product()
    task_purchases = sync_to_async(Purchase.objects.filter, thread_sensitive=False)(product=product)
    task_sales = sync_to_async(Sale.objects.filter, thread_sensitive=False)(product=product)
    sales, purchases = await asyncio.gather(task_sales, task_purchases)
    total_sales, total_purchases = await asyncio.gather(async_get_sale(sales), async_get_purchase(purchases))
    return total_sales, total_purchases

