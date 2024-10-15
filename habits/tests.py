from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(owner=self.user,
                                          place="at home",
                                          time="13:00:00.300000",
                                          action="drink water",
                                          nice_habit=True,
                                          is_published=True,
                                          related_habit=None,
                                          period="daily",
                                          duration="00:01:00",
                                          award="apple"
                                          )

    def test_habit_retrieve(self):
        """ Тестируем просмотр привычки. """
        url = reverse('habits:habit-get', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        # )
        self.assertEqual(
            data.get("action"), self.habit.action
        )

    def test_habit_create(self):
        """ Тестируем создание привычки. """
        url = reverse('habits:habit-create')
        data = {
            "place": "at home",
            "time": "13:00:00.300000",
            "action": "drink water",
            "nice_habit": False,
            "is_published": False,
            "period": "daily",
            "duration": "00:01:00",
            "related_habit": 1
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

    def test_habit_update(self):
        """ Тестируем редактирование привычки. """
        url = reverse('habits:habit-update', args=(self.habit.pk,))
        data = {
            "period": "weekly"
        }
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("period"), "weekly"
        )

    def test_habit_delete(self):
        """ Тестируем удаление привычки. """
        url = reverse('habits:habit-delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 0
        )

    def test_habit_list(self):
        """ Тестируем просмотр списка привычек. """
        url = reverse('habits:habit-list')
        response = self.client.get(url)
        data = response.json()

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results":
                [
                    {
                        "id": self.habit.pk,
                        "place": self.habit.place,
                        "time": self.habit.time,
                        "action": self.habit.action,
                        "nice_habit": True,
                        "is_published": True,
                        "period": self.habit.period,
                        "duration": self.habit.duration,
                        "award": self.habit.award,
                        "created_at": self.habit.created_at.strftime(
                            "%Y-%m-%dT%H:%M:%S.%fZ"
                        ),
                        "owner": self.user.pk,
                        "related_habit": None
                    }
                ]
        }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            result, data
        )
