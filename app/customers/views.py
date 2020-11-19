from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics

class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomertDetail(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        registration = self.kwargs['registration']
        return Customer.objects.filter(registration_date=registration)