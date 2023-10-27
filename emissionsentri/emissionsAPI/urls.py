from django.urls import path
from .views import GetEmissions, GetSingleEmissions

urlpatterns = [
    path("emissions/", GetEmissions.as_view()),
    path("emissions/<int:pk>", GetSingleEmissions.as_view()),
]