import datetime

from django.db import models


class Branch(models.Model):
    """A model class representing branches of the multinational company."""

    branch_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["country", "city"],
                name="unique_branch",
            )
        ]


class Team(models.Model):
    """A model class representing teams of a specific branch."""

    class TeamType(models.TextChoices):
        ADMINISTRATIVE = "Administrative"
        DESIGN = "UX/UI Design"
        SOFTWARE_DEVELOPMENT = "Software Development"
        HR = "HR"

    branch = models.ForeignKey(
        Branch, on_delete=models.DO_NOTHING, null=True, related_name="teams"
    )
    team_id = models.AutoField(primary_key=True)
    team_type = models.CharField(
        max_length=45, choices=TeamType.choices, default=TeamType.SOFTWARE_DEVELOPMENT
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["branch", "team_type"],
                name="unique_team",
            )
        ]


class Employee(models.Model):
    """A model class that represent an employee from a specific team."""

    employee_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name="employees",
    )
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email_address = models.EmailField(null=False)
    birthdate = models.DateField(null=False)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True)

    @property
    def is_birthday(self) -> True:
        now = datetime.datetime.now()
        return (now.day, now.month) == (self.birthdate.day, self.birthdate.month)

    @property
    def age(self) -> int:
        today = datetime.datetime.now().date()
        has_had_birthday = (today.month, today.day) >= (
            self.birthdate.month,
            self.birthdate.day,
        )
        return today.year - self.birthdate.year - (0 if has_had_birthday else 1)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
