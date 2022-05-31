# # Create your views here.
import json
from rest_framework import viewsets
from .models import Provider, Geojson
from .serializers import ProviderSerializer, GeojsonSerializer
from . import serializers

class ProviderViewset(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


class GeojsonViewset(viewsets.ModelViewSet):
    queryset = Geojson.objects.all()
    serializer_class = serializers.GeojsonSerializer

    def get_queryset(self):
        # queryset = super().get_queryset()
        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)
        if lat == None or lng == None:
            queryset = Geojson.objects.all()
            return queryset

    #searching with reegix  inside json
        queryset = Geojson.objects.filter(geojson__iregex=r"('|\\\")lat('|\\\")\s*:\s*"+str(lat)+"\s*,\s*('|\\\\\")lng('|\\\\\")\s*:\s*"+str(lng))
        return queryset
