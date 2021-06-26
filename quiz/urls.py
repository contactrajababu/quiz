from django.urls import path
from . import views
urlpatterns = [
path('quizlist',views.createquiz.as_view()),
path('question',views.createquestion.as_view()),
]