from rest_framework import serializers
from . models  import employee

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields = ('firstname','lastname')
        #fields = __all__


