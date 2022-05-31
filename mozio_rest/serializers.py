# mozio_providers/serializers
from rest_framework import serializers
from .models import Provider, Geojson


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone_number',
                  'language', 'currency' )

class GeojsonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geojson
        fields = ('id', 'provider_id', 'name', 'price',
                  'geojson' )
