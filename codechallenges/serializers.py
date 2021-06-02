from typing_extensions import Required
from rest_framework import serializers
from codechallenges.models import Author, Question, Submission, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["firstname", "lastname"]


class QuestionSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, required=False)
    authors = AuthorSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = (
            "title",
            "body",
            "format",
            "answer",
            "release_date",
            "expiration_date",
            "difficulty",
            "categories",
            "authors",
        )


class QuestionHiddenSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = (
            "title",
            "body",
            "format",
            "release_date",
            "expiration_date",
            "difficulty",
            "categories",
            "authors",
        )


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ("email", "correct", "answer", "question", "attempts")
