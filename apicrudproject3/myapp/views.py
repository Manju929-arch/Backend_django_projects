from django.shortcuts import render
from rest_framework.views import APIView
from myapp.models import Student
from myapp.serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StudentList(APIView):
    def get(self,request):
       s =  Student.objects.all()
       s1 =  StudentSerializers(s,many = True)
       return Response(s1.data)
    
    def post(self, request):
        s1 = StudentSerializers(data = request.data)
        if s1.is_valid():
            s1.save()
            return Response(s1.data,status = status.HTTP_201_CREATED)
        return Response(s1.errors, status = status.HTTP_400_BAD_REQUEST)
    
class StudentDetails(APIView):
    def get(self, request, id):
        try:
            s = Student.objects.get(id =id)
        except s.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        s1 = StudentSerializers(s)
        return Response(s1.data,status = status.HTTP_200_OK)
    
    def put(self, request , id):
        try:
            s = Student.objects.get(id = id)
        except s.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        s1 = StudentSerializers(s, data = request.data)
        if s1.is_valid():
            s1.save()
            return Response(s1.data, status = status.HTTP_200_OK)
        return Response(s1.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request , id):
        try:
            s = Student.objects.get(id = id)
        except s.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        s.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
