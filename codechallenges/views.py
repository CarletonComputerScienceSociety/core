from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Question, Submission
from .serializers import (
    QuestionSerializer,
    QuestionHiddenSerializer,
    SubmissionSerializer,
)
from datetime import datetime, timedelta


@csrf_exempt
def SubmissionList(request):
    if request.method == "POST":
        data = JSONParser().parse(request)

        try:
            question = Question.objects.get(pk=data["question"])
        except Question.DoesNotExist:
            return HttpResponse(status=500)

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

            return JsonResponse(serializer.data, status=200)
        except Submission.DoesNotExist:
            data["attempts"] = 1

        if question.answer == data["answer"]:
            data["correct"] = True
        else:
            data["correct"] = False

        serializer = SubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=500)


@csrf_exempt
def QuestionList(request):
    if request.method == "GET":
        questions = Question.objects.filter(
            release_date__lte=datetime.date(datetime.now())
        )
        serializer = QuestionHiddenSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=500)


@csrf_exempt
def CurrentQuestionList(request):
    if request.method == "GET":
        questions = Question.objects.filter(
            release_date__lte=datetime.date(datetime.now()),
            expiration_date__gt=datetime.date(datetime.now()),
        )
        serializer = QuestionHiddenSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=500)


@csrf_exempt
def ExpiredQuestionList(request):
    if request.method == "GET":
        questions = Question.objects.filter(
            expiration_date__lt=datetime.date(datetime.now())
        )
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=500)


@csrf_exempt
def QuestionDetails(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=500)

    if question.release_date <= datetime.date(datetime.now()):
        if request.method == "GET":
            serializer = QuestionHiddenSerializer(question)
            return JsonResponse(serializer.data)
        else:
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=500)
