from . import models
import datetime


def employees_celebrating_bday(
    status: bool=True,
    avoid_team_type: str | None ='Administrative',
    **kwargs
    ) -> models.Employee:
    """A function that returns a list of Employee objects whose birthday is today.

    Args:
        status (bool, optional): Employment status is either active or inactive. Defaults to True.
        avoid_team_type (str, optional): Team that doesn't receive emails.
        Defaults to 'Administrative'.

    Returns:
        models.Employee: A list of Employee objects.
    """
    now = datetime.datetime.now()
    employees = models.Employee.objects.filter(
        birthdate__day=now.day, 
        birthdate__month=now.month,
        active=True).exclude(
            team__team_type=avoid_team_type
        )
    return employees


def employees_not_celebrating_bday(
    status: bool=True,
    avoid_team_type: str | None = 'Administrative',
    **kwargs
    ) -> models.Employee:
    """A function that returns a list of Employee objects whose birthday IS NOT today.

    Args:
        status (bool, optional): Employment status is either active or inactive. Defaults to True.
        avoid_team_type (str, optional): Team that doesn't receive emails.
        Defaults to 'Administrative'.

    Returns:
        models.Employee: A list of Employee objects.
    """
    now = datetime.datetime.now()
    employees = models.Employee.objects.filter(
        active=True).exclude(
            team__team_type=avoid_team_type,
            birthdate__day=now.day,
            birthdate__month=now.month,
        )
    return employees