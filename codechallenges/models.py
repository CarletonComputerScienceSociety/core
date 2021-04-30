from django.db import models


class CodeChallengeEvent(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    format = models.CharField(
        choices=(
            ("t", "text"),
            ("h", "html"),
            ("m", "mathjax"),
        ),
        max_length=1,
    )
    answer = models.CharField(max_length=150)
    release_date = models.DateField()
    expiration_date = models.DateField()
    difficulty = models.CharField(
        choices=(
            ("e", "easy"),
            ("m", "medium"),
            ("h", "hard"),
        ),
        max_length=1, null=True, blank=True,
    )
    event = models.ForeignKey(
        CodeChallengeEvent, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.title


class Submission(models.Model):
    email = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    correct = models.BooleanField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True
    )
