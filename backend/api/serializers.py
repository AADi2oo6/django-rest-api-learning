from rest_framework import serializers #importing serialisers
from students.models import student #importing models

#now create a class for student serialisers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__" # we want all fields to be serialize
