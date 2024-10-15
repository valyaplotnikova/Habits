from rest_framework import serializers

from habits.models import Habit
from habits.validators import (DurationValidator, OnlyAwardOrRelatedValidator, OnlyISNiceValidator,
                               IsNiceHabitValidator, PeriodValidator)


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [DurationValidator('duration',),
                      OnlyAwardOrRelatedValidator('related_habit', 'award',),
                      OnlyISNiceValidator('related_habit',),
                      IsNiceHabitValidator('nice_habit'),
                      PeriodValidator('period'),
                      ]


class HabitPublishedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'period', 'duration',)
