from rest_framework import viewsets
from . import models


class BranchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Branch.objects.all()
    serializer = None
    

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = None