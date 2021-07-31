from .models import EnrollmentProjection
from rest_framework import serializers


class EnrollmentProjectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnrollmentProjection
        fields = ['url', 'id', 'course_code', 'course_name', 'r2_value', 'area', 'estimated_amount']