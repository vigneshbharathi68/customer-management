from customers.models import Customers
from rest_framework import viewsets, permissions, response
from rest_framework.views import APIView
from .serializers import CustomerSerializer

# Customer viewset


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer


class AddCustomer(APIView):
    queryset = Customers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer

    def postData(self, request):

        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            form_data = serializer.save()

            content_data = {}
            content_data['message'] = "customer Details updated successfully"
            return response.Response(content_data)

        else:
            content_data = {}
            content_data['error'] = "Invalid customer Details credentials"
            return response.Response(content_data)
