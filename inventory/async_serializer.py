from datetime import datetime
from decimal import Decimal
import concurrent.futures

from inventory.models import Sale, Purchase, Product
import asyncio

from asgiref.sync import sync_to_async, async_to_sync

from inventory.utils import discount

@sync_to_async
def get_sale():
    print(f'beginning sale- {datetime.now().time()}')
    product = Product.objects.all().order_by('?')[0]
    sales = Sale.objects.filter(product=product)
    total_sales = 0
    for sale in sales:
        sale.price = sale.price * Decimal((1 - 0.10))
        sale.save()
        total_sales += sale.price
    print(f'finished sale- {datetime.now().time()}')
    return total_sales


@sync_to_async
def get_purchase():
    print(f'beginning purchase- {datetime.now().time()}')
    product = Product.objects.all().order_by('?')[0]
    purchases = Purchase.objects.filter(product=product)
    total_purchases = 0
    for purchase in purchases:
        if purchase.product.pk == 3:
            purchase.price = 0
            purchase.save()
        if purchase.product.pk == 10:
            purchase.price = purchase.prince * Decimal(1 - 0.10)
            purchase.save()
            total_purchases += purchase.price
    print(f'finished purchase- {datetime.now().time()}')
    return total_purchases


async def async_discount():
    sales = asyncio.create_task(get_sale())
    purchases = asyncio.create_task(get_purchase())

    sales, purchases = await asyncio.gather(sales, purchases)
    return sales, purchases

