from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50),
    email = models.EmailField(unique=True, null=True)
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=255)
    
#The name of survey 
class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
# Represent the question itself
class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

#Possible options for question 
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

#store responses
class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model for authentication
    answer = models.TextField()

    def __str__(self):
        return self.answer
    
    