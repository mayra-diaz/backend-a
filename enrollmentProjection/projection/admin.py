from django.contrib import admin

from .models import EnrollmentProjection

class EnrollmentProjectionAdmin(admin.ModelAdmin):
    fields = ['url', 'id', 'course_code', 'course_name', 'academic_period', 'area', 'estimated_amount']

admin.site.register(EnrollmentProjection, EnrollmentProjectionAdmin)
