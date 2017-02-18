from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet

from api.models import Profile, Home, Offer
from api.serializers import UserSerializer, GroupSerializer, ProfileSerializer, HomeSerializer, OfferSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class HomeViewSet(ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer





