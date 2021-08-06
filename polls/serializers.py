from rest_framework import serializers
from polls.models import Poll, MultipleChoiceQuestion


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ["body"]


class PollSerializer(serializers.ModelSerializer):
    questions = MultipleChoiceQuestionSerializer(many=True, required=False)

    class Meta:
        model = Poll
        fields = ["title", "questions"]
