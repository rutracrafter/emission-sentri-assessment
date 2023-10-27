from rest_framework import serializers
from .models import Emission

class EmissionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Emission
        fields = "__all__"