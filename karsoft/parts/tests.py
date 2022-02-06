from django.test import TestCase
from .models import Meals, Reserve
from django.utils import timezone
import datetime


future_question = Reserve(input_date=timezone.now() + datetime.timedelta(days=30))

class QuestionModelTests(TestCase):
    def check(self):
        b = Reserve.objects.filter(phone='155550a01')[:1]
        if b:
            return True

        self.assertIs(b.check(), True)