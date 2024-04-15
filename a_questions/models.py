from django.db import models

class Question(models.Model):
    # question_number = models.SmallAutoField(unique=True)
    question_text = models.TextField(max_length=500)

    def __str__(self):
        return str(self.question_text)