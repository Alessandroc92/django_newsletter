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
    team = serializers.PrimaryKeyRelatedField(
        queryset=models.Team.objects.all(),
        required=True,
        allow_null=False,
    )
    team_detail = TeamSerializer(source="team", read_only=True)

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
            "team",
            "team_detail",
        )
        read_only_fields = ("employee_id", "age", "is_birthday")

    def validate_birthdate(self, value) -> int:
        more_than_70 = datetime.datetime.now().date().year - value.year >= 70
        if more_than_70:
            raise serializers.ValidationError("You should be retired by now!")
        return value
