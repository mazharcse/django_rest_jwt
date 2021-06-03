from apiapp.models import Country, State, Address
from rest_framework import serializers

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'latitude', 'longitude', 'code']

class SimpleCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class StateSerializer(serializers.HyperlinkedModelSerializer):
    country = SimpleCountrySerializer(many=False,read_only=True)
    class Meta:
        model = State
        fields = ['name', 'country']

class StateDetailSerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer(many=False,read_only=True)
    class Meta:
        model = State
        fields = ['name', 'country']


class SimpleStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['name']

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    state = SimpleStateSerializer(many=False, read_only=True)
    class Meta:
        model = Address
        fields = ['name', 'house_number', 'road_number','state']

class AddressDetailSerializer(serializers.HyperlinkedModelSerializer):
    country = SimpleCountrySerializer(many=False, read_only=True)
    state = StateSerializer(many=False, read_only=True)

    class Meta:
        model = Address
        fields = ['name', 'house_number','road_number', 'state', 'country']
