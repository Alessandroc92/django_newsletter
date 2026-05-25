import datetime

from newsletter import employees
from newsletter.employees import services

from . import models


def template_bday(employee: employees.models.Employee, **kwargs) -> models.Template:
    """A function that creates a Template model starting from Employee data.

    Args:
        employee (employees.models.Employee): An Employee model object.

    Returns:
        models.Template: A Template model object
    """
    subject = f"Happy Birthday, Dear {employee.first_name}!!!"
    body = f"""
        Hey {employee.first_name}!
        
        A little bird told us that today you're turning {employee.age}!
        Our great family wants to thank you for your service in this special day.
        We hope you and your fellow people working at the {employee.team.team_type}
        in {employee.team.branch.city} will have a chance to celebrate together.
        
        All the best from your favorite Company,
        
        Global HR
    """
    return models.Template(
        recipient=employee.email_address,
        subject=kwargs.get("custom_subject_bday") or subject,
        body=kwargs.get("custom_body_bday") or body,
    )


def template_bday_info(
    employee: employees.models.Employee,
    bday_employees: list[employees.models.Employee],
    **kwargs,
) -> models.Template:


    subject = f"There are some colleagues celebrating their birthday today!!!"

    bday_employees_lines = [
        f"Name: {bde.first_name} {bde.last_name} - E-mail Address: {bde.email_address}"
        for bde in bday_employees
    ]

    body_lines = [
        f"Hey {employee.first_name}!",
        "",
        f"Today there are {len(bday_employees)} colleagues celebrating their birthday!",
        "Don't forget to contact them all! Here's a handy list for you:",
        "",
        *bday_employees_lines,
        "",
        "Thanks,",
        "",
        "Global HR",
    ]

    body = "\n".join(body_lines)
    return models.Template(
        recipient=employee.email_address,
        subject=kwargs.get("custom_subject_no_bday") or subject,
        body=kwargs.get("custom_body_no_bday") or body,
    )


def create_templates_to_send(**kwargs):
    bday_employees = services.employees_celebrating_bday(**kwargs)
    bday_templates = [
        template_bday(employee=employee, **kwargs) for employee in bday_employees
    ]
    non_bday_employees = services.employees_not_celebrating_bday(**kwargs)
    non_bday_templates = [
        template_bday_info(employee=employee, bday_employees=bday_employees, **kwargs)
        for employee in non_bday_employees
    ]
    return [*bday_templates, *non_bday_templates]


def create_emails_from_templates(**kwargs):
    template_objects = create_templates_to_send(**kwargs)
    templates = models.Template.objects.bulk_create(template_objects)
    notification_run = models.NotificationRun.objects.create(
        n_recipients=len(templates),
    )
    email_logs = [
        models.EmailLog(
            template=template, notification_run_id=notification_run.notification_run_id
        )
        for template in templates
    ]
    models.EmailLog.objects.bulk_create(email_logs)
    return tuple(
        (email.subject, email.body, None, [email.recipient]) for email in templates
    )
