from rest_framework import serializers
from .models import Employee




class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


    def validate(self, data):
        a = data["ename"]
        b = a.title()
        if b!=True:
            raise serializers.ValidationError("name error")
        return a

    def validate_esal(self,value):
        if value>1000:
            raise serializers.ValidationError("salary error")

