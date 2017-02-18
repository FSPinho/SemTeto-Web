
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django.conf.urls import url, include
from rest_framework import routers

from api.views import UserViewSet, GroupViewSet, OfferViewSet, HomeViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'home', HomeViewSet)
router.register(r'offer', OfferViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token)
]