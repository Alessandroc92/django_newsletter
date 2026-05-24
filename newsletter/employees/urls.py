from django.urls import path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('employees', viewset=views.EmployeeViewSet)
urlpatterns = router.urls