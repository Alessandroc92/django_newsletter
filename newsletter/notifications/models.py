from django.db import models


class NotificationRun(models.Model):
    notification_run_id = models.AutoField(primary_key=True)
    n_recipient = models.PositiveIntegerField(null=False)
    notification_date = models.DateTimeField(null=False, auto_now=True)
