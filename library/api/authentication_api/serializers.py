from rest_framework import serializers
from authentication.models import CustomUser
from order.models import Order
from api.order_api.serializers import OrderSerializer


class UserSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'email', 'password', 'role', 'is_active', 'orders')
