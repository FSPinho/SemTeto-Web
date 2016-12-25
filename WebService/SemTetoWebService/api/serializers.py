from django.contrib.auth.models import User, Group
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from api.models import Profile, Home, Offer


class UserSerializer(HyperlinkedModelSerializer):
    houses = HyperlinkedRelatedField(many=True, read_only=True, view_name='home-detail')
    offers = HyperlinkedRelatedField(many=True, read_only=True, view_name='offer-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups', 'houses', 'offers')


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProfileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class HomeSerializer(HyperlinkedModelSerializer):
    offer = HyperlinkedRelatedField(many=False, read_only=True, view_name='home-detail')

    class Meta:
        model = Home
        fields = '__all__'


class OfferSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'