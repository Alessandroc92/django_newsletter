from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializers


class ResultPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class NotificationRunViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.NotificationRun.objects.all()
    serializer_class = serializers.NotificationRunSerializer


class EmailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.EmailLog.objects.all()
    serializer_class = serializers.EmailLogSerializer
    

class TemplateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Template.objects.all()
    serializer_class = serializers.TemplateSerializer
