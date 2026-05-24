from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializers


class ResultPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class BranchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer
    

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    pagination_class = ResultPagination