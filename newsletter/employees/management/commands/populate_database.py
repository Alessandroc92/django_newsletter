from newsletter.employees.models import Branch, Team, Employee
from django.core.management.base import BaseCommand
import random
import datetime

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
        