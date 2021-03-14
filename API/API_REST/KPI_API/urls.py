from django.urls import path
from KPI_API import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("investments/", views.AllInvestmentsViewSet.as_view()),
    path("investments/ville/<str:ville>", views.CityInvestmentsViewSet.as_view()),
    path("investments/etat/<str:etat>", views.StateInvestmentViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)