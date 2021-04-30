from django.test import TestCase
from rest_framework.test import APIRequestFactory
from codechallenges.models import Question, Submission
from .views import SubmissionList
import datetime

# Create your tests here.


class SubmissionTestCase(TestCase):
    def test_submission(self):
        question1 = Question.objects.create(
            title="Yeet",
            body="Blaghjdklahgjfkl",
            format="t",
            answer="Yote",
            release_date=datetime.date.today(),
            expiration_date=datetime.date(2022, 4, 29),
        )
        factory = APIRequestFactory()

        # Makes and verifies successful request (first attempt)
        attempt1 = factory.post(
            "/api/codechallenges/submissions/",
            {
                "email": "robertbabaev@cmail.carleton.ca",
                "question": 1,
                "answer": "Yate",
            },
            format="json",
        )
        response = SubmissionList(attempt1)
        self.assertEquals(response.status_code, 201)

        # Verifies submission creation
        submissions = list(Submission.objects.all())
        self.assertEquals(submissions[0].attempts, 1)

        # Makes and verifies successful request (second attempt)
        attempt2 = factory.post(
            "/api/codechallenges/submissions/",
            {
                "email": "robertbabaev@cmail.carleton.ca",
                "question": 1,
                "answer": "Yote",
            },
            format="json",
        )
        response = SubmissionList(attempt2)
        self.assertEquals(response.status_code, 200)

        # Verifies submission update
        submissions = list(Submission.objects.all())
        self.assertEquals(submissions[0].attempts, 2)

    def test_unique_together(self):
        question1 = Question.objects.create(
            title="Yeet",
            body="Blaghjdklahgjfkl",
            format="t",
            answer="Yote",
            release_date=datetime.date.today(),
            expiration_date=datetime.date(2022, 4, 29),
        )

        # Verify question 1 is created
        self.assertNotEquals(question1, None)

        submission1 = Submission.objects.create(
            email="test123@gmail.com",
            answer="Yote",
            correct=True,
            question=question1,
            attempts=5,
        )

        # Verify submission 1 is created
        self.assertNotEquals(submission1, None)

        # This should pass because it's not a dupe!
        submission2 = Submission.objects.create(
            email="test124@gmail.com",
            answer="Y0te",
            correct=False,
            question=question1,
            attempts=5,
        )

        # Verify submission 3 is created
        self.assertNotEquals(submission2, None)

        # This should fail due to duplicate checking
        with self.assertRaises(Exception):
            submission3 = Submission.objects.create(
                email="test123@gmail.com",
                answer="Yate",
                correct=False,
                question=question1,
                attempts=5,
            )
