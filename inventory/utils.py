import os
import pickle
from datetime import datetime
from decimal import Decimal

import redis
from asgiref.sync import sync_to_async
from django.template.defaultfilters import lower
from django.views.decorators.cache import cache_page

from asyncbalance.settings import CACHES
from inventory.models import Sale, Purchase, Product

cache_args = dict(host=os.environ.get('DB_HOST'),
                  password=os.environ.get('REDIS_PASSWORD'))
cache = redis.Redis(**cache_args)


def get_sale(sales):
    print(f'beginning sale - {datetime.now().time()}')
    total_sales = 0
    for sale in sales:
        sale.price = sale.price * Decimal((1 - 0.10))
        sale.save()
        total_sales += sale.price
    print(f'finished sale - {datetime.now().time()}')
    return total_sales


def get_purchase(purchases):
    print(f'beginning purchase - {datetime.now().time()}')
    total_purchases = 0
    for purchase in purchases:
        purchase.price = purchase.price * Decimal(1 - 0.15)
        purchase.save()
        total_purchases += purchase.price
    print(f'finished purchase - {datetime.now().time()}')
    return total_purchases


def random_product():
    if cache.exists('product'):
        product = pickle.loads(cache.get('product'))
    else:
        product = Product.objects.all().order_by('?')[0]
        cache.set('product', pickle.dumps(product))
    return product.pk


def discount():
    product = random_product()
    sales = Sale.objects.filter(product=product)
    total_sales = get_sale(sales)
    purchases = Purchase.objects.filter(product=product)
    total_purchases = get_purchase(purchases)
    return total_sales, total_purchases
