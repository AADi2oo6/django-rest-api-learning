from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from students.models import student 
from . serializers import StudentSerializer # 1st need to import serializer
from rest_framework.response import Response # for reciving respocne
from rest_framework import status # for checking responce status 
from rest_framework.decorators import api_view


#imports for class based views
from .serializers import EmployeeSerializer
from employees.models import Employee
from rest_framework.views import APIView 
from django.http import Http404 # does not come in class APIView

# imports for Mixins
from rest_framework import mixins , generics, viewsets


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


@api_view(['GET','PUT','DELETE']) #In Order to use GET 
def studentDetailView(request,pk):# Accepting primiry key from the url
    try:
        student_data = student.objects.get(id = pk) #filtering data based on primary key
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= StudentSerializer(student_data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT': 
        # (student_data,data = request.data) using this line to pre_populate the existing Student data
        serializer = StudentSerializer(student_data, data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 

# class Employees(APIView):
#     def get(self,request):
#         emp_data = Employee.objects.all()
#         serializer = EmployeeSerializer(emp_data,many = True)
#         return Response(serializer.data,status = status.HTTP_200_OK)
#     def post(self,request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
# class EmployeeDetail(APIView):
#         def get_object(self,pk):
#             try:
#                emp_data = Employee.objects.get(id=pk)
#                return emp_data
#             except Employee.DoesNotExist:
#                raise Http404
           
#         def get(self,request,pk):
#             emp_data = self.get_object(pk)
#             serializer = EmployeeSerializer(emp_data)
#             return Response(serializer.data,status = status.HTTP_200_OK)
        
#         def put(self,request,pk):
#             emp_data = self.get_object(pk)
#             serializer = EmployeeSerializer(emp_data,data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status = status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
#         def delete(self,request,pk):
#             emp_data = self.get_object(pk)
#             emp_data.delete()
#             return Response(status= status.HTTP_204_NO_CONTENT)
           
"""#   USING MIXINS # 
"""
'''class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    # importing both list and create model mixins for using both get and post requests
    queryset = Employee.objects.all() # important to use this for fetching the data :
    serializer_class  = EmployeeSerializer
    
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)


class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all() # this two lins are important for fetching and serializing
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)'''


# Using Generics
'''class Employees(generics.ListAPIView,generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"'''


# Using View Sets: 

#viewsets.ViewSet
'''class EmployeeViewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk = None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK) 

    def update(self,request, pk = None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error_messages)
    def delete(self,request,pk = None):
        employee = get_object_or_404(Employee,pk = pk)
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 
'''

# 2. using viewset.ModelViewSet
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    












