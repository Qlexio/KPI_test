from django.shortcuts import render
from django.http import Http404
from .models import JsonDataset
from .serializers import JsonDatasetSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class AllInvestmentsViewSet(APIView):

    def get(self, request, format=None):
        investment = JsonDataset.objects.all()
        serializer = JsonDatasetSerializer(investment, many= True)
        return Response(serializer.data)

class CityInvestmentsViewSet(APIView):

    def get_object(self, ville):
        try:
            return JsonDataset.objects.filter(ville= ville)
        except JsonDataset.DoesNotExist:
            raise Http404

    def get(self, request, ville, format=None):
        investment = self.get_object(ville)
        serializer = JsonDatasetSerializer(investment, many= True)
        return Response(serializer.data)

class StateInvestmentViewSet(APIView):

    def get_object(self, etat):
        try:
            return JsonDataset.objects.filter(etat_d_avancement= etat)
        except JsonDataset.DoesNotExist:
            raise Http404

    def get(self, request, etat, format=None):
        investment = self.get_object(etat)
        serializer = JsonDatasetSerializer(investment, many=True)
        return Response(serializer.data)

class CodeInvestmentsViewSet(APIView):

    def get_object(self, code):
        try:
            return JsonDataset.objects.filter(codeuai= code)
        except JsonDataset.DoesNotExist:
            raise Http404

    def get(self, request, code, format=None):
        investment = self.get_object(code)
        serializer = JsonDatasetSerializer(investment, many=True)
        return Response(serializer.data)