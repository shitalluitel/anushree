import json

from django.views.generic.base import View
# from momohub.mixins import HttpResponseMixin
from rest_framework import generics

from products.api.serializers import TireSerializer
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


class TireDetailView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Product.objects.all()
    serializer_class = TireSerializer
    # lookup_field = 'id'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs

        kw_id = kwargs.get('pk')
        return Product.objects.get(id=kw_id, is_deleted=False)

