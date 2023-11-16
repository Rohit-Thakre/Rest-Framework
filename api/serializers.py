from rest_framework import serializers
from api.models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.ReadOnlyField()

    class Meta: 
        model = Company
        # fields = '__all__'
        exclude = ['by']
        
