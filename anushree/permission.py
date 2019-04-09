# import the logging library
import logging

# Get an instance of a logger
from rest_framework import permissions

logger = logging.getLogger(__name__)


#
#
# class SampleModelPermissions(permissions.DjangoObjectPermissions):
#     perms_map = {
#         'GET': ['%(app_label)s.view_%(model_name)s'],
#         'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
#         'HEAD': ['%(app_label)s.view_%(model_name)s'],
#         'POST': ['%(app_label)s.add_%(model_name)s'],
#         'PUT': ['%(app_label)s.change_%(model_name)s'],
#         'PATCH': ['%(app_label)s.change_%(model_name)s'],
#         'DELETE': ['%(app_label)s.delete_%(model_name)s'],
#     }
#
#     logger.info('in SampleModelPermissions')
#
#     def has_permission(self, request, view):
#         logger.info('in SampleModelPermissions has_permission')
#         if request.method in permissions.SAFE_METHODS:
#             logger.info('SampleModelPermissions: has_permission: listing samples for user: ' + str(request.user.id))
#             return True
#         elif request.method == 'POST':
#             suggested_owner = None
#             try:
#                 logger.info(
#                     'SampleModelPermissions: has_permission: request dict should have a suggested owner: ' + str(
#                         dict(request.data.iterlists())))
#                 suggested_owner = int(dict(request.data.iterlists())['owner_id'][0])
#             except:
#                 logger.error('SampleModelPermissions: has_permission: request made without owner_id: ' + str(
#                     dict(request.data.iterlists())))
#                 return False
#             return request.user.id == suggested_owner
#
#     def has_object_permission(self, request, view, obj):
#         logger.info('in SampleModelPermissions has_object_permission')
#
#         if request.method in permissions.SAFE_METHODS:
#             return request.user == obj.owner or True  # need to modify so can see own stuff
#         elif request.method == 'PATCH':
#             return request.user == obj.owner
#         elif request.method == 'DELETE':
#             return request.user == obj.owner
#         return False

class CustomObjectPermissions(permissions.DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
