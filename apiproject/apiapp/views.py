from django.shortcuts import render
from rest_framework import viewsets
from apiapp.models import Country, State, Address
from rest_framework import viewsets
from apiproject.serializers import CountrySerializer, StateSerializer, AddressSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'code']

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer