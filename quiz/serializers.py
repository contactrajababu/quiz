from rest_framework import serializers
from . models  import *

class quizserializer(serializers.ModelSerializer):
    class Meta:
        model=quiz
        fields ='__all__'

class questionsserializer(serializers.ModelSerializer):
    class Meta:
        model=questions
        fields ='__all__'
