import datetime
import logging
import random

import django.db
from django.core.management.base import BaseCommand

from newsletter.employees.models import Branch, Employee, Team

logger = logging.getLogger(__name__)


FIRST_NAMES = ("John", "Sarah", "Nassim", "Faroq", "Clara")
LAST_NAMES = ("Smith", "Drinkwater", "Rogue", "Taleb", "Dent")


def random_birthday(begin_year:int =1957, end_year: int=2008) -> datetime.date:
    random_month = random.randint(1, 12)
    random_day = random.randint(1,28) if random_month == 2\
        else (random.randint(1,30) if random_month in (4,6,9,11) else random.randint(1,31))
    return datetime.date(
                        year=random.randint(begin_year, end_year),
                        month=random_month,
                        day=random_day,
                    )


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            branches = [
                Branch(country="Italy", city="Milan"),
                Branch(country="Italy", city="Rome"),
                Branch(country="Italy", city="Florence"),
                Branch(country="United Kingdom", city="London"),
                Branch(country="USA", city="New York"),
                Branch(country="China", city="Bejing"),
                Branch(country="Hungary", city="Budapest"),
                Branch(country="Brazil", city="Rio De Janeiro"),
                Branch(country="Japan", city="Tokyo"),
            ]

            Branch.objects.bulk_create(branches)
            branches_objects = Branch.objects.all()

            teams = [
                Team(team_type=team_name, branch=branch)
                for team_name in [
                    "Administrative",
                    "UX/UI Design",
                    "Software Development",
                    "HR",
                ]
                for branch in branches
            ]

            Team.objects.bulk_create(teams)
            team_objects = Team.objects.all()

            employees = [
                Employee(
                    first_name=random.choice(FIRST_NAMES),
                    last_name=random.choice(LAST_NAMES),
                    birthdate=random_birthday(),
                    active=random.randint(0, 1),
                    team=random.choice(team_objects),
                )
                for _ in range(10000)
            ]
            for employee in employees:
                employee.team = random.choice(team_objects)
                employee.email_address = f"{employee.first_name}_{employee.last_name}{random.randint(1000, 9999)}@company.com"
                employee.save()
        except django.db.IntegrityError:
            logger.info("The DB is already populated with the necessary data.")
