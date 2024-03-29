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


class Author(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Question(models.Model):
    title = models.CharField(max_length=150)
    preview = models.TextField()
    body = models.TextField()
    format = models.CharField(
        choices=(
            ("text", "text"),
            ("html", "html"),
            ("mathjax", "mathjax"),
        ),
        max_length=10,
    )
    answer = models.CharField(max_length=150)
    release_date = models.DateField()
    expiration_date = models.DateField()
    difficulty = models.CharField(
        choices=(
            ("easy", "easy"),
            ("medium", "medium"),
            ("hard", "hard"),
        ),
        max_length=10,
        null=True,
        blank=True,
    )
    event = models.ForeignKey(
        CodeChallengeEvent, on_delete=models.CASCADE, blank=True, null=True
    )

    categories = models.ManyToManyField(Category, blank=True)
    authors = models.ManyToManyField(Author, blank=True)

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
        # validate_carleton_email(self.email)
        super(Submission, self).save(*args, **kwargs)

    class Meta:
        unique_together = (
            "email",
            "question",
        )
