from rest_framework import serializers
from codechallenges.models import Question, Submission

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("title", "body", "format", "answer", "release_date", "expiration_date")

class QuestionHiddenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("title", "body", "format")

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ("email", "correct", "answer", "question")
