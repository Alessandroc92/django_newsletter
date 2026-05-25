from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from . import models, serializers, tasks


class ResultPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100


class NotificationRunViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.NotificationRun.objects.all()
    serializer_class = serializers.NotificationRunSerializer

    @action(detail=False, url_path="send_bday_emails", methods=["post"])
    def activate_email_task(self, request: HttpRequest):
        tasks.send_happy_bday_emails.enqueue(**request.data)
        return Response(data="The send bday email task has been executed as requested.")


class EmailLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.EmailLog.objects.all()
    serializer_class = serializers.EmailLogSerializer
    pagination_class = ResultPagination


class TemplateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Template.objects.all()
    serializer_class = serializers.TemplateSerializer
