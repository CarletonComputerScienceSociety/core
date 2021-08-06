from django.db import models

# Create your models here.


class Poll(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    access_date = models.DateField()

    def questions(self):
        print(self)
        return self.multiple_choice_questions.filter()

    def __str__(self):
        return self.title


class MultipleChoiceQuestion(models.Model):
    body = models.TextField()

    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="multiple_choice_questions",
    )

    def __str__(self):
        return self.body


class MultipleChoiceOption(models.Model):
    body = models.TextField()

    multiple_choice_question = models.ForeignKey(
        MultipleChoiceQuestion, on_delete=models.CASCADE, blank=True, null=True
    )
