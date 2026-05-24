from django.db import models

# Create your models here.
class Branch(models.Model):
    """A model class representing branches of the multinational company."""
    branch_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    

class Team(models.Model):
    """A model class representing teams of a specific branch."""
    class TeamType(models.TextChoices):
        ADMINISTRATIVE = 'Administrative'
        DESIGN = 'UX/UI Design'
        SOFTWARE_DEVELOPMENT = 'Software Development'
        HR = 'HR'
    branch = models.ForeignKey(
        Branch,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='teams'
    )
    team_id = models.AutoField(primary_key=True)
    team_type = models.CharField(
        max_length=45,
        choices=TeamType.choices,
        default=TeamType.SOFTWARE_DEVELOPMENT
        )