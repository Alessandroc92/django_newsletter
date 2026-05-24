import datetime
from rest_framework import serializers
from . import models

        
class NotificationRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Template
        fields = (
            'notification_run_id',
            'n_recipients',
            'notification_date',
        )
    
        
class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Template
        fields = (
            'template_id',
            'template_recipient'
            'template_subject',
            'template_body',
        )


class EmailLogSerializer(serializers.ModelSerializer):
    template = TemplateSerializer(read_only=True)
    notification_run = NotificationRunSerializer(read_only=True)

    class Meta:
        model = models.EmailLog
        fields = (
            'notification_id',
            'template',
            'notification_run',
            'sent_at',
        )