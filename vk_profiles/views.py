from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from vk_profiles.handlers.create_api import create_api
from vk_profiles.handlers.get_cur_user import get_cur_user
from vk_profiles.models import Profile
from vk_profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSetп):
    permission_classes = (permissions.AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    """
        GET token by vk_id
    """
    @action(detail=False)
    def token(self, request):
        vk_id = request.data.get('vk_id')
        if not bool(vk_id and vk_id.strip()):
            return Response({'error': 'vk_id not set!'})
        access_token = Profile.objects.filter(vk_id=vk_id).values('access_token')
        return Response(access_token)

    """
        POST create token by login and password
    """
    @action(detail=False, methods=['post'], name="create-access-token")
    def create_access_token(self, request):
        login = request.data.get('login')
        password = request.data.get('password')
        if not bool(login and login.strip()):
            return Response({'error': 'login not set!'})
        if not bool(password and password.strip()):
            return Response({'error': 'password not set!'})
        try:
            api, log_stream = create_api(login, password)
            cur_user, url_response = get_cur_user(api, log_stream)
            new_profile = Profile.objects.create()
            new_profile.access_token = url_response.get("access_token")
            new_profile.vk_id = cur_user[0].get("id")
            new_profile.last_name = cur_user[0].get("last_name")
            new_profile.first_name = cur_user[0].get("first_name")
            new_profile.save()
            return Response(ProfileSerializer(new_profile).data)
        except Exception as e:
            return Response({'error': str(e)})
