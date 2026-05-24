from django.db import models

# Create your models here.
class Branch(models.Model):
    """A model class representing branches of the multinational company."""
    branch_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
