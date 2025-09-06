from django.urls import path
from . import views
urlpatterns = [
    path("",views.api_home),# localhost:8000/api
    path("students/",views.studentView),
    path("students/<int:pk>/",views.studentDetailView), #fetching data based on primary key

    path("employees/",views.Employees.as_view()),
    #Whenever we have to use Class as view we have to use .as_view() after name of class
    path("employees/<int:pk>/",views.EmployeeDetail.as_view() )
]
