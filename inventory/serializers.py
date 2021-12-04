from rest_framework.fields import SerializerMethodField

from inventory.models import Purchase, Sale, Client, Product, Provider
from rest_framework import serializers







class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    provider = SerializerMethodField()
    product = SerializerMethodField()

    class Meta:
        model = Purchase
        fields = ['provider', 'product', 'price', 'date']

    def get_provider(self, instance):
        return ProviderSerializer()

    def get_product(self, instance):
        return ProviderSerializer()


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    client = SerializerMethodField()
    product = SerializerMethodField()

    class Meta:
        model = Sale
        fields = ['client', 'product', 'price', 'date']

    def get_client(self, instance):
        return instance.client.name

    def get_product(self, instance):
        return instance.product.name


class ProviderSerializer(serializers.Serializer):
    class Meta:
        model = Provider
        fields = '__all__'

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'

class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = '__all__'
