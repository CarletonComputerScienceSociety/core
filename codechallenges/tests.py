from django.urls import reverse
from django.test import TestCase
from django.test.client import Client
from rest_framework.test import APIRequestFactory, APITestCase
from codechallenges.models import Author, Category, Question, Submission
from .views import SubmissionList

import datetime

# Create your tests here.


class QuestionTestCase(APITestCase):
    def setUp(self) -> None:
        self.category1 = Category.objects.create(
            title="Algorithms", body="SPEED IS KEY"
        )
        self.category2 = Category.objects.create(
            title="Cryptography", body="KEY IS KEY"
        )
        self.author1 = Author.objects.create(firstname="John", lastname="Wick")
        self.author2 = Author.objects.create(firstname="Doom", lastname="Guy")
        self.question1 = Question.objects.create(
            title="Yeet",
            body="Blaghjdklahgjfkl",
            format="t",
            answer="Yote",
            release_date=datetime.date.today(),
            expiration_date=datetime.date(2022, 4, 29),
            difficulty="e",
        )
        self.question2 = Question.objects.create(
            title="Yoet",
            body="Blaghjdklahgjfkl",
            format="t",
            answer="Yete",
            release_date=datetime.date.today(),
            expiration_date=datetime.date(2022, 4, 29),
            difficulty="e",
        )
        self.unreleased = Question.objects.create(
            title="aaaa",
            body="LIPSUM",
            format="t",
            answer="LOREM IPSUM DOLOR SIT AMET",
            release_date=datetime.date.today() + datetime.timedelta(days=365),
            expiration_date=datetime.date(2022,4,29),
            difficulty="e"
        )
        self.client = Client()
        return super().setUp()

    def test_categories(self):
        self.question1.categories.add(self.category1)  # Added
        self.question1.categories.add(self.category2)  # Added
        self.question2.categories.add(self.category1)  # Not Added
        self.assertEquals(len(self.question1.categories.all()), 2)

    def test_authors(self):
        self.question1.authors.add(self.author1)  # Added
        self.question1.authors.add(self.author2)  # Added
        self.question2.authors.add(self.author1)  # Not Added
        self.assertEquals(len(self.question1.authors.all()), 2)

    """
    def test_get_individual_question(self):
        get_q1 = self.client.get(reverse("question-view", args=(1,)))
        self.assertEquals(get_q1.status_code, 200)

    def test_get_nonexistent_question(self):
        get_nonexistent = self.client.get(reverse("question-view", args=(5,)))
        self.assertEquals(get_nonexistent.status_code, 404)

    def test_get_unreleased_question(self):
        get_unreleased = self.client.get(reverse("question-view", args=(3,)))
        self.assertEquals(get_unreleased.status_code, 404)
    """

class SubmissionTestCase(APITestCase):
    def setUp(self) -> None:
        self.question1 = Question.objects.create(
            title="Yeet",
            body="Blaghjdklahgjfkl",
            format="t",
            answer="Yote",
            release_date=datetime.date.today(),
            expiration_date=datetime.date(2022, 4, 29),
            difficulty="e",
        )
        self.client = Client()
        return super().setUp()

    """
    def test_submission(self):

        # Makes and verifies successful request (first attempt)
        attempt1 = self.client.post(
            reverse("submission-view"),
            {
                "email": "robertbabaev@cmail.carleton.ca",
                "question": 1,
                "answer": "Yate",
            },
            content_type="application/json"
        )
        self.assertEquals(attempt1.status_code, 201)

        # Verifies submission creation
        submissions = list(Submission.objects.all())
        self.assertEquals(submissions[0].attempts, 1)

        # Makes and verifies successful request (second attempt)
        attempt2 = self.client.post(
            reverse("submission-view"),
            {
                "email": "robertbabaev@cmail.carleton.ca",
                "question": 1,
                "answer": "Yote",
            },
            content_type="application/json"
        )
        self.assertEquals(attempt2.status_code, 200)

        # Verifies submission update
        submissions = list(Submission.objects.all())
        self.assertEquals(submissions[0].attempts, 2)
    """

    def test_unique_together(self):

        # Verify question 1 is created
        self.assertNotEquals(self.question1, None)

        submission1 = Submission.objects.create(
            email="test123@cmail.carleton.ca",
            answer="Yote",
            correct=True,
            question=self.question1,
            attempts=5,
        )

        # Verify submission 1 is created
        self.assertNotEquals(submission1, None)

        # This should pass because it's not a dupe!
        submission2 = Submission.objects.create(
            email="test124@cmail.carleton.ca",
            answer="Y0te",
            correct=False,
            question=self.question1,
            attempts=5,
        )

        # Verify submission 3 is created
        self.assertNotEquals(submission2, None)

        # This should fail due to duplicate checking
        with self.assertRaises(Exception):
            submission3 = Submission.objects.create(
                email="test123@cmail.carleton.ca",
                answer="Yate",
                correct=False,
                question=self.question1,
                attempts=5,
            )

    def test_validate_email(self):
        with self.assertRaises(Exception):
            submission1 = Submission.objects.create(
                email="test1@gmail.com",
                answer="Yate",
                correct=False,
                question=self.question1,
                attempts=5,
            )
        with self.assertRaises(Exception):
            submission2 = Submission.objects.create(
                email="carleton.ca",
                answer="Yate",
                correct=False,
                question=self.question1,
                attempts=5,
            )
        with self.assertRaises(Exception):
            submission3 = Submission.objects.create(
                email="robert@carleton.ca",
                answer="Yate",
                correct=False,
                question=self.question1,
                attempts=5,
            )
        submission4 = Submission.objects.create(
            email="robertbabaev@cmail.carleton.ca",
            answer="Yate",
            correct=False,
            question=self.question1,
            attempts=5,
        )
        submission5 = Submission.objects.create(
            email="robertbabaev@cunet.carleton.ca",
            answer="Yate",
            correct=False,
            question=self.question1,
            attempts=5,
        )
        self.assertNotEquals(submission4, None)
        self.assertNotEquals(submission5, None)
