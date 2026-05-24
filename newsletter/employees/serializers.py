from rest_framework import serializers
from . import models


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = (
            'branch_id',
            'country',
            'city',
        )


class TeamSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    class Meta:
        model = models.Team
        fields = (
            'team_id',
            'team_type',
            'branch'
        )