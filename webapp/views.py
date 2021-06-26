from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employee
from . serializers import employeeserializer

class employeelist(APIView):
    def get(self,request):
        employees1 = employee.objects.all()
        serializers = employeeserializer(employees1,many=True)
        return Response(serializers.data)
    def post(self,request):
        emp_data = request.data
        try:
            employee.objects.get(firstname=emp_data['firstname'])
            return Response("data already exists")
        except employee.DoesNotExist:
            new_emp = employee.objects.create(firstname=emp_data['firstname'],lastname=emp_data['lastname'],emp_id=employee.objects.all().count() +1)
            new_emp.save()
            serializers = employeeserializer(new_emp)
        return Response(serializers.data)

