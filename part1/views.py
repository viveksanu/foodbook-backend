from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from part1.models import Question
from part1.models import Answer
from part1.serializers import QuestionSerializer
from part1.serializers import AnswerSerializer
from rest_framework.decorators import api_view
from django.db.models import F
@api_view(['GET'])
def list_question(request):
    questions = Question.objects.all()
    question_serializer = QuestionSerializer(questions, many=True)
    return JsonResponse(question_serializer.data, safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def save_answer(request):
    
    try: 
        answer_data = JSONParser().parse(request)
        qno=answer_data["question"]
        question = Question.objects.get(pk=qno) 
        count=Answer.objects.filter(question=qno).count()
        if count==0:
            answer_serializer = AnswerSerializer(data=answer_data) 
        else:
            answer=Answer.objects.get(question=qno)
            answer_serializer = AnswerSerializer(answer,data=answer_data) 
        
        if answer_serializer.is_valid(): 
                answer_serializer.save() 
                return JsonResponse(answer_serializer.data,status=status.HTTP_200_OK) 
        return JsonResponse(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Question.DoesNotExist: 
        return JsonResponse({'message': 'The question does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
     
    
    
    