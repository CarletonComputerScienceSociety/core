from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from .models import Question, Submission
from .serializers import (
    QuestionSerializer,
    QuestionHiddenSerializer,
    SubmissionSerializer,
)
from datetime import datetime, timedelta


class SubmissionList(generics.GenericAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()

    def post(self, request):
        data = request.data
        print(data)
        print(data["question"])
        try:
            question = Question.objects.get(pk=data["question"])
        except Question.DoesNotExist:
            return Response(
                {"data": {}, "errors": "Invalid ID"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # Need to check if submission exists before creating one
        try:
            submission = Submission.objects.get(
                question=data["question"], email=data["email"]
            )
            submission.attempts += 1

            if question.answer == data["answer"]:
                submission.correct = True
            else:
                submission.correct = False

            submission.answer = data["answer"]
            submission.save()

            serializer = SubmissionSerializer(submission)

            return Response(
                {"data": serializer.data, "errors": {}}, status=status.HTTP_200_OK
            )
        except Submission.DoesNotExist:
            data["attempts"] = 1

        if question.answer == data["answer"]:
            data["correct"] = True
        else:
            data["correct"] = False

        serializer = SubmissionSerializer(data=data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"data": serializer.data, "errors": {}},
                    status=status.HTTP_201_CREATED,
                )
        except ValidationError:
            return Response(
                {"data": {}, "errors": "Invalid Email."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response(
            {"data": serializer.data, "errors": "Invalid Input."},
            status=status.HTTP_200_OK,
        )


class QuestionList(generics.ListAPIView):

    queryset = Question.objects.filter(release_date__lte=datetime.date(datetime.now()))
    serializer_class = QuestionHiddenSerializer


class CurrentQuestionList(generics.ListAPIView):

    queryset = Question.objects.filter(
        release_date__lte=datetime.date(datetime.now()),
        expiration_date__gt=datetime.date(datetime.now()),
    )
    serializer_class = QuestionHiddenSerializer


class ExpiredQuestionList(generics.ListAPIView):

    queryset = Question.objects.filter(
        release_date__lte=datetime.date(datetime.now()),
        expiration_date__gt=datetime.date(datetime.now()),
    )
    serializer_class = QuestionSerializer


class QuestionDetails(generics.RetrieveAPIView):

    queryset = Question.objects.filter(release_date__lte=datetime.date(datetime.now()))
    serializer_class = QuestionHiddenSerializer
