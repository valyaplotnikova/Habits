from datetime import timedelta

from rest_framework import serializers


class DurationValidator:
    """
    Валидация по времени выполнения привычки.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)
        if duration > timedelta(seconds=120):
            raise serializers.ValidationError("Длительность привычки не может быть больше 120 секунд")
