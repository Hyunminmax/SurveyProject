from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=100, default='')
    ages = models.SmallIntegerField(choices=((1, '10s'), (2, '20s'), (3, '30s'), (4, '40s'), (5, '50s'), (6, '60s'), (7, '70s over')), default=0)
    gender = models.SmallIntegerField(choices=((1, 'Male'), (2, 'Female')), default=0)
    answer = models.CharField(max_length=120)

    def get_data_send_to_list(self):
        return [int(char) for char in self.answer]
