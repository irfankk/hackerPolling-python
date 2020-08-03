from rest_framework import permissions


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view, ):
        if request.user.is_superuser:
            return True


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user