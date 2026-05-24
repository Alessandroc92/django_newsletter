import datetime
from . import models
from newsletter import employees


def template_bday(employee: employees.models.Employee) -> models.Template:
    """A function that creates a Template model starting from Employee data.

    Args:
        employee (employees.models.Employee): An Employee model object.

    Returns:
        models.Template: A Template model object
    """
    subject = f'Happy Birthday, Dear {employee.first_name}!!!'
    body = f'''
        Hey {employee.first_name}!
        
        A little bird told us that today you're turning {employee.age}!
        Our great family wants to thank you for your service in this special day.
        We hope you and your fellow people working at the {employee.team.team_type}
        in {employee.team.branch.city} will have a chance to celebrate together.
        
        All the best from your favorite Company,
        
        Global HR
    '''
    return models.Template(
        recipient=employee.email_address,
        subject=subject,
        body=body,
        )