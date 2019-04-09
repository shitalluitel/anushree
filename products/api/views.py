import json

from django.views.generic.base import View
# from momohub.mixins import HttpResponseMixin
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions

from anushree.permission import CustomObjectPermissions
from products.api.serializers import TireSerializer, TubeSerializer
from products.models import Product


# class ProductList(HttpResponseMixin, View):
#
#     # def get_queryset(self):
#     #     qs = Product.objects.filter(cate)
#     #     # self.queryset = qs
#     #     return qs
#     #
#     # def get_object(self, id=None):
#     #     if id is None:
#     #         return None
#     #     qs = self.get_queryset().filter(id=id)
#     #     if qs.count() == 1:
#     #         return qs.first()
#     #     return None
#
#     def get(self, request, slug, *args, **kwargs):
#         # data = json.loads(request.body)
#         # category = data.get('category', None)
#
#         qs = Product.objects.filter(category__slugs__iexact=slug)
#
#         qs_count = qs.count()
#         print(qs_count)
#         if qs_count > 0:
#             json_data = qs.serialize()
#         else:
#             json_data = json.dumps([{'error': True}])
#
#         return self.render_to_response(json_data)


class TireDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoObjectPermissions]
    authentication_classes = [SessionAuthentication]
    # perms_map =
    queryset = Product.objects.filter(category__name__icontains='tire')
    serializer_class = TireSerializer

    # lookup_field = 'id'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs

        kw_id = kwargs.get('pk')
        return Product.objects.get(id=kw_id, is_deleted=False)


class TubeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoObjectPermissions]
    authentication_classes = [SessionAuthentication]
    queryset = Product.objects.filter(category__name__icontains='tube', )
    serializer_class = TubeSerializer

    # lookup_field = 'id'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs

        kw_id = kwargs.get('pk')
        return Product.objects.get(id=kw_id, is_deleted=False)


class TireListView(generics.ListCreateAPIView):
    permission_classes = [DjangoObjectPermissions]
    authentication_classes = [SessionAuthentication]
    queryset = Product.objects.filter(category__name__icontains='tire')
    serializer_class = TireSerializer


class TubeListView(generics.ListCreateAPIView):
    permission_classes = [DjangoObjectPermissions]
    authentication_classes = [SessionAuthentication]
    queryset = Product.objects.filter(category__name__icontains='tube', )
    serializer_class = TubeSerializer


# class TireListView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [SessionAuthentication]
#     queryset = Product.objects.filter(category__name__icontains='tire')
#     serializer_class = TireSerializer
