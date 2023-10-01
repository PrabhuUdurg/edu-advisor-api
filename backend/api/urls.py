from django.urls import path
from .views import registration, login, create_survey, list_surveys, survey_detail, add_question, questions, options_create, options_list
urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', login, name='login'),
    path('survey-create/', create_survey, name='create-survey'),
    path('survey/', list_surveys, name='list-surveys'),
    path('survey-update/', survey_detail, name='survey-detail'),
    path('questions-create/', add_question, name='questions'),
    path('questions-list/', questions, name='question-create'),
    path('options-create/', options_create, name='options-create'),
    path('options-list', options_list, name='options_list'),    
]