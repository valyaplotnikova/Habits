from rest_framework import serializers


class DurationValidator:
    """
    Валидация по времени выполнения привычки.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)
        if duration:
            duration_time = (duration.hour * 60 + duration.minute) * 60 + duration.second
            if duration_time > 120:
                raise serializers.ValidationError(
                    "Длительность привычки не может быть больше 120 секунд"
                )


class OnlyAwardOrRelatedValidator:
    """
    Ограничение по выбору одного из значений:
    связанной привычки или вознаграждения.
    """
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        if dict(value).get("related_habit") and dict(value).get("award"):
            raise serializers.ValidationError(
                "Можно заполнить либо поле Вознаграждение, "
                "либо поле Связанная привычка"
            )


class OnlyISNiceValidator:
    """
    Ограничение по выбору связанной привычки.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get("connection_habit"):
            if not value.get("habit_is_pleasant"):
                raise serializers.ValidationError(
                    "Связанная привычка может быть только приятной")


class IsNiceHabitValidator:
    """
       Ограничение по выбору приятной привычки.
       У приятной привычки не может быть связанной привычки и вознаграждения.
       """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        nice_habit = dict(value).get(self.field)
        if nice_habit:
            if dict(value).get('award') or dict(value).get('related_habit'):
                raise serializers.ValidationError(
                    "У приятной привычки не может быть "
                    "связанной привычки и вознаграждения"
                )


class PeriodValidator:
    """
    Ограничение по периоду выполнения привычки.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period = dict(value).get(self.field)
        if period != 'daily' and period != 'weekly':
            raise serializers.ValidationError(
                'Нельзя выполнять привычку реже одного раза в неделю'
            )
