from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # look for field called "get_my_discount"

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            # 'get_discount',
            'my_discount'
        ]

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
