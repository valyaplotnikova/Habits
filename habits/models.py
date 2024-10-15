from datetime import timedelta

from django.db import models

from config.settings import AUTH_USER_MODEL
from users.models import NULLABLE


class Habit(models.Model):
    """
    Модель привычки.
    """
    PERIOD = {
        'daily': 'ежедневно',
        'weekly': 'еженедельно'
    }

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='создатель привычки',
        **NULLABLE
    )
    place = models.CharField(
        max_length=150,
        verbose_name='место выполнения привычки'
    )
    time = models.TimeField(
        verbose_name='время выполнения привычки'
    )
    action = models.CharField(
        max_length=255,
        verbose_name='действие для привычки'
    )
    nice_habit = models.BooleanField(
        verbose_name='признак приятной привычки'
    )
    is_published = models.BooleanField(
        verbose_name='признак публичной привычки'
    )
    related_habit = models.ForeignKey(
        'self',
        models.CASCADE,
        verbose_name='связная привычка',
        **NULLABLE
    )
    period = models.CharField(
        max_length=150,
        choices=PERIOD,
        default='daily',
        verbose_name='период выполнения'
    )
    duration = models.TimeField(
        default=timedelta(seconds=120),
        verbose_name='время на выполнение'
    )
    award = models.CharField(
        max_length=150,
        verbose_name='вознаграждение',
        **NULLABLE)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания привычки'
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
