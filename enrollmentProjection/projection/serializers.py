from projection.models import EnrollmentProjection
from rest_framework import serializers


class EnrollmentProjectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnrollmentProjection
        fields = ['url', 'id', 'course_code', 'course_name', 'academic_period', 'area', 'estimated_amount']

