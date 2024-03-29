from rest_framework import serializers

from apps.api.error_messages import (
    STATUS_NAME_LEN_ERROR_MESSAGE,
    CATEGORY_NAME_LEN_ERROR_MESSAGE,
    PRIORITY_NAME_LEN_ERROR_MESSAGE
)

from apps.todo.models import (
    Category,
    Status,
    Priority,
    Task,
    SubTask
)


class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'created_by',
            'category',
            'status',
            'priority',
            'deadline',
            'created_at'
        ]

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3 or len(value) > 30:
            raise serializers.ValidationError(
                STATUS_NAME_LEN_ERROR_MESSAGE
            )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 4 or len(value) > 25:
            raise serializers.ValidationError(
                CATEGORY_NAME_LEN_ERROR_MESSAGE
            )

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 4 or len(value) > 25:
            raise serializers.ValidationError(
                PRIORITY_NAME_LEN_ERROR_MESSAGE
            )
