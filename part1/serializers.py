from rest_framework import serializers 
from part1.models import Question
from part1.models import Answer

class QuestionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Question
        fields = ('id',
                  'question_text')


class AnswerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Answer
        fields = ('id','question',
                  'answer_text')
