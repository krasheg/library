from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework import viewsets
from authentication.models import CustomUser
from .serializers import UserSerializer
from api.order_api.serializers import OrderSerializer
from order.models import Order


# Create your views here.
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UserApiView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        if instance.role == 1:
            instance.is_superuser = True
            instance.is_staff = True
        instance.save()


class OrderAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    serializer_class = OrderSerializer

    def get_queryset(self):
        filter_value = self.kwargs['user_id']
        queryset = Order.objects.filter(user_id=filter_value)
        return queryset
