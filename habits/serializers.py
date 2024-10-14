from rest_framework import serializers

from habits.models import Habit
from habits.validators import DurationValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [DurationValidator(field='duration')]
