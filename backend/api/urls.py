from rest_framework.routers import DefaultRouter

from api.views import UsFuelViewSet, UsCityViewSet

router = DefaultRouter()
router.register('fuels', UsFuelViewSet, basename='fuels')
router.register('cities', UsCityViewSet, basename='cities')

urlpatterns  = router.urls