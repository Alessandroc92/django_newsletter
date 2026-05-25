from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("email_logs", viewset=views.EmailLogViewSet)
router.register("templates", viewset=views.TemplateViewSet)
router.register("notification_runs", viewset=views.NotificationRunViewSet)
urlpatterns = router.urls
