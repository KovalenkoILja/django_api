from rest_framework import serializers
from .models import Profile


# Serializers define the API representation.
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'vk_id', 'first_name', 'last_name', 'access_token', 'created', 'modified')

