from django.contrib import admin

# Register your models here.
from . models import *
admin.site.register(quiz)
admin.site.register(category)
admin.site.register(questions)
admin.site.register(possibleanswers)
admin.site.register(quizRespoonse)

