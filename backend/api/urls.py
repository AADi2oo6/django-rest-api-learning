from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employees')


urlpatterns = [
    # path("",views.api_home),# localhost:8000/api
    path("students/",views.studentView),
    path("students/<int:pk>/",views.studentDetailView), #fetching data based on primary key

    # path("employees/",views.Employees.as_view()),
    # #Whenever we have to use Class as view we have to use .as_view() after name of class
    # path("employees/<int:pk>/",views.EmployeeDetail.as_view() ),


    # ViewSets: 
    path("",include(router.urls)),

    path("blogs/",views.BlogsView.as_view()),
    path("blogs/<int:pk>",views.BlogDetailView.as_view()),
    path("comments/",views.CommentsView.as_view()),
    path("comments/<int:pk>",views.CommentsDetailView.as_view()),


]
