from django.shortcuts import render
from rest_framework import status, generics
from .models import Emission
from .serializers import EmissionsSerializer


# Create your views here.
class GetEmissions(generics.ListAPIView):
    queryset = Emission.objects.all()
    serializer_class = EmissionsSerializer

class GetSingleEmissions(generics.RetrieveAPIView):
    queryset = Emission.objects.all()
    serializer_class = EmissionsSerializer