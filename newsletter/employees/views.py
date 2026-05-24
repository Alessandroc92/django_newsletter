from rest_framework import viewsets
from . import models
from . import serializers


class BranchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Branch.objects.all()
    serializer = serializers.BranchSerializer
    

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = None
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = None