from django.shortcuts import render
from projection.models import EnrollmentProjection
from rest_framework import viewsets
from rest_framework import permissions
from projection.serializers import EnrollmentProjectionSerializer

class ActionBasedPermission(permissions.AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """

    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False

class EnrollmentProjectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EnrollmentProjection.objects.all()
    serializer_class = EnrollmentProjectionSerializer
    permission_classes = [permissions.IsAuthenticated]
