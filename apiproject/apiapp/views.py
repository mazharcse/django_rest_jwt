from django.shortcuts import render
from rest_framework import viewsets
from apiapp.models import Country, State, Address
from rest_framework import viewsets
from apiproject.serializers import CountrySerializer, StateSerializer, AddressSerializer, AddressDetailSerializer
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

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country__name','name']

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state__name', 'road_number', 'house_number']

class AddressDetailViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state__name', 'road_number', 'house_number']