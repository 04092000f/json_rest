from rest_framework import routers
from mozio_rest.views import ProviderViewset, GeojsonViewset


router = routers.DefaultRouter()
router.register(r'providers', ProviderViewset)
router.register(r'geojsons', GeojsonViewset)