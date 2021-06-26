from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
class createquiz(APIView):
    def get(self,request):
        quizlist = quiz.objects.all()
        serializers = quizserializer(quizlist,many=True)
        return Response(serializers.data)
    def post(self,request):
        quiz_data = request.data
        try:
            quiz.objects.get(quizname=quiz_data['quizname'])
            return Response("data already exists")
        except quiz.DoesNotExist:
            try:
                category1 = category.objects.get(categoryid=quiz_data['category'])
                new_quiz = quiz.objects.create(quizid=quiz.objects.all().count()+1,quizname=quiz_data['quizname'],createdby=quiz_data['createdby'],totalquestion=quiz_data['totalquestion'],
                                              category=category1,quizdate=quiz_data['quizdate'])
                new_quiz.save()
                serializers = quizserializer(new_quiz)
            except category.DoesNotExist:
                return Response("Category does not exist")
        return Response(serializers.data)

class createquestion(APIView):
    def get(self,request):
        questionlist = questions.objects.all()
        serializers = questionsserializer(questionlist,many=True)
        return Response(serializers.data)
    def post(self,request):
        ques_data = request.data
        try:
            questions.objects.get(questext=ques_data['questext'])
            return Response("Question already exists")
        except questions.DoesNotExist:
            try:
                quiz1 = quiz.objects.get(quizid=ques_data['quiz'])
                new_ques = questions.objects.create(quesid=questions.objects.all().count()+1,questext=ques_data['questext'],answer=ques_data['answer'],
                                              quiz=quiz.add(quiz1))
                new_ques.save()
                serializers = questionsserializer(new_ques)
            except quiz.DoesNotExist:
                return Response("quiz does not exist")
        return Response(serializers.data)