from . import models
import datetime


def employees_celebrating_bday(
    status: bool=True,
    avoid_team_type: str='Administrative',
    ) -> models.Employee:
    now = datetime.datetime.now()
    employees = models.Employee.objects.filter(
        birthdate__day=now.day, 
        birthdate__month=now.month,
        active=True).exclude(
            team__team_type=avoid_team_type
        )
    return employees