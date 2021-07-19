from django.urls import path, include
from .import views
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('enrollmentProjection', views.EnrollmentProjectionView)



urlpatterns = [
    path('', include(router.urls))

]