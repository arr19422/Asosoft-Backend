from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        verify_user = User.objects.get(id=token.user_id)
        if not verify_user.is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'token': token.key,
                'user_id': user.pk
            })