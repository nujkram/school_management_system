from rest_framework import serializers

from departments.models.department import Department as Master


class DepartmentPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )

class DepartmentPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )

class DepartmentPrivateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )

class DepartmentPrivateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )