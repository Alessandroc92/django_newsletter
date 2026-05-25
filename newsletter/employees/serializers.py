import datetime

from rest_framework import serializers

from . import models


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = (
            "branch_id",
            "country",
            "city",
        )


class TeamSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = models.Team
        fields = ("team_id", "team_type", "branch")


class EmployeeSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = models.Employee
        fields = (
            "employee_id",
            "first_name",
            "last_name",
            "birthdate",
            "email_address",
            "active",
            "age",
            "is_birthday",
            "branch",
            "team",
        )

    def validate_birthdate(self, value) -> int:
        more_than_70 = datetime.datetime.now().date().year - value.year >= 70
        if more_than_70:
            raise serializers.ValidationError("You should be retired by now!")
        return value
