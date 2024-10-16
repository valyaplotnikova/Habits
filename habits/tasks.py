import datetime
import pytz

from celery import shared_task
from config import settings
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_reminder_tg():
    """
    Функция отправки напоминания о выполнении привычки в телеграм.
    """
    zone = pytz.timezone(settings.CELERY_TIMEZONE)
    now = datetime.datetime.now(zone)
    future = now + datetime.timedelta(minutes=10)

    habits = Habit.objects.all()

    for habit in habits:
        user_id = habit.owner.tg_chat_id

        if now.time().strftime("%H:%M:%S") < habit.time.strftime("%H:%M:%S") < future.time().strftime("%H:%M:%S"):
            message = f"Не забудьте. Вы должны {habit.action} в {habit.time} в {habit.place}"
            if user_id:
                send_telegram_message(user_id, message)
