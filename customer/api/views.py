from rest_framework import generics

from customer.api.serializers import CustomerSerializer
from customer.models import Customer


class CustomerDetailView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # lookup_field = 'id'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs

        kw_id = kwargs.get('pk')
        return Customer.objects.filter(pk=kw_id).first()
