import django_filters 
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    # Create a filter for the 'designation' field for case-insensitive matching
    position = django_filters.CharFilter(field_name='position', lookup_expr='iexact')
 
    # Create a filter for the 'name' field for case-insensitive "contains" search
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')

    #create a filter for the 'id' field for range serach
    # id= django_filters.RangeFilter(field_name = 'id')


    # initially id min and max will show invalild name on the page as they are not initial filelds of the model 
    # Hence we have to use label 
    id_min = django_filters.CharFilter(method = 'filter_id_by_range', label = "From Emp Id")
    id_max = django_filters.CharFilter(method = 'filter_id_by_range', label = "To Emp Id")

    class Meta:
        model = Employee
        # Specify the fields that this FilterSet will work with
        fields = ['position','emp_name','id_min','id_max']

    def filter_id_by_range(self,queryset,name,value):
        if name =='id_min':
            # __get = grater then or equal to : means if id_min return emp_id graterthen or equal to value
            return queryset.filter(emp_id__gte = value)
        elif name == 'id_max':
            # __lte = less then or equal to  
            return queryset.filter(emp_id__lte= value)
        return queryset
        
