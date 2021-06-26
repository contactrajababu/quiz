from django.db import models

# Create your models here.
class category(models.Model):
    categoryid=models.IntegerField(primary_key =True)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class quiz(models.Model):
    quizid = models.IntegerField(primary_key=True)
    quizname= models.CharField(max_length=100)
    createdby = models.CharField(max_length=100)
    quizdate = models.DateField()
    totalquestion = models.IntegerField()
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.quizname

class questions(models.Model):
    quesid = models.IntegerField(primary_key=True)
    questext = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    quiz = models.ManyToManyField(quiz)

    def __str__(self):
        return str(self.quesid)

class possibleanswers(models.Model):
    ques = models.ForeignKey(questions,on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)


class quizRespoonse(models.Model):
    responseid = models.IntegerField(primary_key=True)
    ques = models.ForeignKey(questions,on_delete=models.CASCADE)
    givenanswer = models.CharField(max_length=100)
    status= models.BooleanField(default=False)






