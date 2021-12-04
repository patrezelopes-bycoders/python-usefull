import decimal
from datetime import datetime
from random import random, randrange

from django.core.management.base import BaseCommand, CommandError
from inventory.models import Product, Provider, Client, Purchase, Sale
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = '--all to create 10000 sales and 10000 purchase from 100 client and 100 providers using 100 products'

    def create_all(self):
        self.create_random_product(1000)
        self.create_random_client(100)
        self.create_random_provider(100)
        self.create_random_purchase(10000)
        self.create_random_sale(10000)
        print("created")

    def add_arguments(self, parser):
        parser.add_argument('--product', nargs='+', type=int)
        parser.add_argument('--client', nargs='+', type=int)
        parser.add_argument('--provider', nargs='+', type=int)
        parser.add_argument('--purchase', nargs='+', type=int)
        parser.add_argument('--sale', nargs='+', type=int)
        parser.add_argument('--all', action='store_true')

    def handle(self, *args, **options):
        try:
            product = options.get('product')
            if product:
                self.create_random_product(product[0])
        finally:
            product = None

        try:
            client = options.get('client')
            if client:
                self.create_random_client(client[0])
        finally:
            client = None
        try:
            provider = options.get('provider')
            if provider:
                self.create_random_provider(provider[0])
        finally:
            provider = None

        try:
            purchase = options.get('purchase')
            if purchase:
                self.create_random_purchase(purchase[0])
        finally:
            purchase = None

        try:
            sale = options.get('sale')
            if sale:
                self.create_random_sale(sale[0])
        finally:
            sale = None

        try:
            if options.get('all'):
                self.create_all()
        finally:
            sale = None


    def create_random_product(self, args):
        for product in range(1, args+1):
            name = f'Product {product}'
            Product.objects.create(name=name)
            print("product created")

    def create_random_provider(self, args):
        for provider in range(1, args+1):
            name = f'Provider {provider}'
            Provider.objects.create(name=name)
            print("provider created")

    def create_random_client(self, args):
        for client in range(args+1):
            name = f'Client {client}'
            Client.objects.create(name=name)
            print("client created")

    def create_random_purchase(self, args):
        for purchase in range(1, args+1):
            provider = Provider.objects.order_by('?')[0]
            product = Product.objects.order_by('?')[0]
            price = decimal.Decimal(randrange(100, 10000) / 100)
            date = datetime(day=randrange(1, 28), month=randrange(1, 12), year=randrange(2020, 2021))
            Purchase.objects.create(provider=provider,
                                    product=product,
                                    price=price,
                                    date=date)
            print("created")

    def create_random_sale(self, args):
        for sale in range(1, args+1):
            client = Client.objects.order_by('?')[0]
            product = Product.objects.order_by('?')[0]
            price = decimal.Decimal(randrange(100, 10000) / 100)
            date = datetime(day=randrange(1, 28), month=randrange(1, 12), year=randrange(2020, 2021))
            Sale.objects.create(client=client,
                                    product=product,
                                    price=price * (1 + randrange(1, 10)),
                                    date=date)
            print("created")
