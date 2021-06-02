from django.core.validators import validate_email
from django.db import models

from .validators import validate_carleton_email


class CodeChallengeEvent(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()

    # questions = models.ManyToManyField(Question)  # Django auto-validates duplicates

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
        max_length=1,
        null=True,
        blank=True,
    )
    event = models.ForeignKey(
        CodeChallengeEvent, on_delete=models.CASCADE, blank=True, null=True
    )

    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title


class Submission(models.Model):
    email = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    correct = models.BooleanField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True
    )
    attempts = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        validate_email(self.email)
        validate_carleton_email(self.email)
        super(Submission, self).save(*args, **kwargs)

    class Meta:
        unique_together = (
            "email",
            "question",
        )
