from django.shortcuts import render
from .models import EnrollmentProjection
from rest_framework import viewsets
from .serializers import EnrollmentProjectionSerializer




class EnrollmentProjectionView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EnrollmentProjection.objects.all()
    serializer_class = EnrollmentProjectionSerializer

