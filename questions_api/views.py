from django.shortcuts import render
from rest_framework import generics
from .serializers import QuestionSerializer
from .serializers import UserAccountSerializer
from .models import Question
from .models import UserAccount

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

# Create your views here.

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

def check_login(request):
    if request.method == 'GET':
        return JsonResponse({})

    if request.method == 'PUT':
        jsonRequest = json.loads(request.body)
        username = jsonRequest['username']
        password = jsonRequest['password']
        if UserAccount.objects.get(username=username):
            user = UserAccount.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'username': user.username})
            else:
                return (JsonResponse({}), 'password not found')
        else:
            return (JsonResponse({'username'}), 'username not found')
