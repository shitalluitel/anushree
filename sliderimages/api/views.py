import json

from django.views.generic.base import View
from rest_framework import generics, mixins, permissions
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# from accounts.api.permissions import IsOwnerOrReadOnly
from anushree.mixins import HttpResponseMixin
from sliderimages.api.serializers import SliderImageSerializer
from sliderimages.models import SliderImage


class SliderImageList(HttpResponseMixin, View):

    def get_queryset(self):
        qs = SliderImage.objects.all()
        # self.queryset = qs
        return qs

    def get_object(self, id=None):
        if id is None:
            return None
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        qs_count = qs.count()
        if qs_count > 0:
            json_data = qs.serialize()
        else:
            json_data = json.dumps([{'error': True}])

        return self.render_to_response(json_data)
