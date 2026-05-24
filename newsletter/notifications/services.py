import datetime
from . import models
from newsletter import employees


def template_bday(employee: employees.models.Employee, **kwargs) -> models.Template:
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
        subject=kwargs.get('subject') or subject,
        body=kwargs.get('body') or body,
        )
    

def template_bday_info(
    employee: employees.models.Employee,
    bday_employees: list[employees.models.Employee],
    **kwargs
    ) -> models.Template:

    bday_employees_data = '\n'.join(
        f'Name: {bde.first_name} {bde.last_name} - E-mail Address: {bde.email_address}' 
        for bde in bday_employees
        )
    subject = f'There are some colleagues celebrating their birthday today!!!'
    body = f'''
        Hey {employee.first_name}!
        
        Today there are {len(bday_employees)} colleagues celebrating their birthday!
        Don't forget to contact them all! Here's a handy list for you:
        
        {bday_employees_data}
        
        Thanks,
        
        Global HR
    '''
    return models.Template(
        recipient=employee.email_address,
        subject=kwargs.get('subject') or subject,
        body=kwargs.get('body') or body,
        )
    

def create_templates_to_send(**kwargs):
    bday_employees = managers.employees_celebrating_bday(**kwargs)
    bday_templates = [
        template_bday(employee=employee, **kwargs) for employee in bday_employees
        ]
    non_bday_employees = managers.employees_not_celebrating_bday(**kwargs)
    non_bday_templates = [
        template_bday_info(employee=employee, bday_employees=bday_employees, **kwargs) 
        for employee in non_bday_employees
        ]
    return [*bday_templates,*non_bday_templates]


def create_emails_from_templates(**kwargs):
    template_objects = create_templates_to_send(**kwargs)
    templates = Template.objects.bulk_create(template_objects)
    notification_run = NotificationRun.objects.create(
        n_recipient=len(templates),
        notification_date=datetime.datetime.now().date()
        )
    email_logs = [
        EmailLog(template=template, notification_run_id=notification_run.notification_run_id)
        for template in templates
        ]
    EmailLog.objects.bulk_create(email_logs)
    return tuple((email.subject, email.body, None,[email.recipient]) for email in templates)