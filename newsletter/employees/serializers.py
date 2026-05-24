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
