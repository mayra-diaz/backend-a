from django.contrib import admin
from .models import EnrollmentProjection
from import_export import resources
from import_export.admin import ImportExportModelAdmin


admin.site.register(EnrollmentProjection)