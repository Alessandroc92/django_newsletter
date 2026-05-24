from newsletter.employees.models import Branch, Team, Employee
from django.core.management.base import BaseCommand
import random
import datetime


FIRST_NAMES = ('John','Sarah','Nassim','Faroq','Clara')
LAST_NAMES = ('Smith','Drinkwater','Rogue','Taleb','Dent')


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        branches = [
            Branch(country='Italy',city='Milan'),
            Branch(country='Italy',city='Rome'),
            Branch(country='Italy',city='Florence'),
            Branch(country='United Kingdom',city='London'),
            Branch(country='USA',city='New York'),
            Branch(country='China',city='Bejing'),
            Branch(country='Hungary',city='Budapest'),
            Branch(country='Brazil',city='Rio De Janeiro'),
            Branch(country='Japan',city='Tokyo'),
        ]
        
        Branch.objects.bulk_create(branches)
        branches_objects = Branch.objects.all()
        
        teams = [
            Team(team_type=team_name,branch=branch) 
            for team_name in [
                'Administrative',
                'UX/UI Design',
                'Software Development',
                'HR'
                ]
            for branch in branches
        ]
        
        Team.objects.bulk_create(teams)
        team_objects = Team.objects.all()

        employees = [
            Employee(
                first_name=random.choice(FIRST_NAMES),
                last_name=random.choice(LAST_NAMES),
                birthdate=datetime.date(
                    year=random.randint(1965,2005),
                    month=random.randint(1,12),
                    day=random.randint(1,28)
                ),
                active=random.randint(0,1),
                team=random.choice(team_objects)
            )
                for _ in range(1000)
        ]
        for employee in employees:
            employee.team = random.choice(team_objects)
            employee.email_address = f'{employee.first_name}_{employee.last_name}{random.randint(1000,9999)}@company.com'
            employee.save()