from django.shortcuts import render
import pyrebase
from .models import User, Survey, Question, Option
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status, generics, serializers
from rest_framework.response import Response
from .serializer import UserSerializer, SurveySerializer, QuestionSerializer, OptionSerializer 
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import firestore
from . import firebase_config
from .firebase_config import firebase_admin, cred
from django.contrib.auth.decorators import login_required


@api_view(['POST'])
@permission_classes([AllowAny])
def registration(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(username=email).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(user)
        return Response(serializer.data)
      
      
# API endpoint for creating a new survey
@api_view(['POST'])
def create_survey(request):
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API endpoint for retrieving all surveys
@api_view(['GET'])
def list_surveys(request):
    surveys = Survey.objects.all()
    serializer = SurveySerializer(surveys, many=True)
    return Response(serializer.data)

# API endpoint for retrieving, updating, or deleting a specific survey

@api_view(['GET', 'PUT', 'DELETE'])
def survey_detail(request, survey_id):
    try:
        survey = Survey.objects.get(id=survey_id)
    except Survey.DoesNotExist:
        return Response({'error': 'Survey not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        survey.delete()
        return Response({'message': 'Survey deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
 
      
@api_view(['POST'])
def add_question(request):
    item = QuestionSerializer(data=request.data)
 
    # validating for already existing data
    if Question.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def questions(request): 
    # checking for the parameters from the URL
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def options_create(request):
    option = OptionSerializer(data=request.data)
    
    if Option.objects.filter(**request.data).exists(): 
        raise serializers.ValidationError('This option already exists')
    
    if option.is_valid():
        option.save()
        return Response(option.data)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def options_list(request):
    options = Option.objects.all()
    serializer = OptionSerializer(options, many=True)
    return Response(serializer.data)