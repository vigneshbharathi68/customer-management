from customers.models import Customers
from rest_framework import viewsets, permissions
from .serializers import CustomerSerializer

# Customer viewset

class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer