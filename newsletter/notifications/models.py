from django.db import models


class NotificationRun(models.Model):
    notification_run_id = models.AutoField(primary_key=True)
    n_recipients = models.PositiveIntegerField(null=False)

    
class Template(models.Model):
    template_id = models.AutoField(primary_key=True)
    recipient = models.EmailField(null=False)
    subject = models.TextField(null=False)
    body = models.TextField(null=False)
    

class EmailLog(models.Model):
    notification_run = models.ForeignKey(
        NotificationRun,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='notification_runs'
        
    )
    notification_id = models.AutoField(primary_key=True)
    template = models.ForeignKey(
        Template,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='templates'
    )
    sent_at = models.DateTimeField(null=False, auto_now=True)
