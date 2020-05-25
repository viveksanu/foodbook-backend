import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Question
from .serializers import QuestionSerializer

client=Client()
class AnswerTest(TestCase):
    def setUp(self):
        self.q1 = Question.objects.create(id=1,
        question_text='question 1')
        #valid
        self.valid_payload = { 
            'question': 1,
            'answer_text': 'Yes'
        }
        #invalid foreign key
        self.invalid_payload_fk = {
            'question': '2',
            'answer_text': 'No'
        }
        #invalid answer_text
        self.invalid_payload_answer_value = {
            'question': '1',
            'answer_text': ''
        }

    def test_create_valid_answer(self):
        response = client.post(
            reverse('save_answer'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_anwser_foreign_key(self):
        response = client.post(
            reverse('save_answer'),
            data=json.dumps(self.invalid_payload_fk),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_invalid_anwser_text(self):
        response = client.post(
            reverse('save_answer'),
            data=json.dumps(self.invalid_payload_answer_value),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      
    

