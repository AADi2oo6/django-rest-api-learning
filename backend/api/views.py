# from django.shortcuts import render
# from django.http import JsonResponse

from students.models import student 
from . serializers import StudentSerializer # 1st need to import serializer
from rest_framework.response import Response # for reciving respocne
from rest_framework import status # for checking responce status 
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        # GET all the data from the student tabel
        student_data = student.objects.all()
        serializer = StudentSerializer(student_data,many= True) # we want multiple data tha's why we set many = True
        return Response(serializer.data, status=status.HTTP_200_OK)
        # the above status codee represents that we have successfully recived data from database 

    elif request.method == 'POST': 
        #Initilizing serializer and asking for data
        serializer = StudentSerializer(data = request.data) # THIS will give a form to insert data

        # if serilizer valied
        if(serializer.is_valid()):
            serializer.save() #save the data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # in this case checking status of creation
        
        #If seirlizer not valied for some reason: return serilizer error (just like data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def api_home(request):
    d ={
        "NAME": "ADITYA SHARMA",
        "PRN" : 12415040
    } 
    return JsonResponse(d)
