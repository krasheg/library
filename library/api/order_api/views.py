from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from api.authentication_api.views import ReadOnly
from order.models import Order
from .serializers import OrderSerializer
# Create your views here.


class OrderApiView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
