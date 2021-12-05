from django.contrib import admin
# Register your models here.

from .models import Sale, Purchase, Product, Provider

admin.site.register(Sale)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Provider)