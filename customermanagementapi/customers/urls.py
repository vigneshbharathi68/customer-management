from rest_framework import routers
from .api import CustomersViewSet, AddCustomer
# from django.urls import path
router = routers.DefaultRouter()
router.register('api/customers', CustomersViewSet, 'customers')
# router.register('api/addcustomers', AddCustomer, 'customers')

urlpatterns = router.urls
# path('api/addCustomer/', AddCustomer.as_view(), name='addcustomer'),
