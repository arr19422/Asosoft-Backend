from rest_framework import viewsets, generics, status
from ..Serializers.changePasswordSerializer import RequestPasswordResetEmailSerializer
from rest_framework.response import Response
from ..Models.userModel import Users
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from ..utils import Util
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import os
from django.http import HttpResponsePermanentRedirect
from api.Serializers.newPasswordSerializer import SetNewPasswordSerializer
from django.contrib.auth.models import User


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RequestPasswordResetEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        print(request.data.get('email'))

        email = request.data.get('email', '')
        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            print(user.user.username)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user.user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hola, \n utiliza el link de la parte inferior para cambiar tu contraseña  \n' + \
                absurl+"?redirect_url="+redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        else:
            print('Correo no encontrado')
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    #serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = Users.objects.get(user__id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url + '?token_valid=False')
                else:
                    return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')

            if redirect_url and len(redirect_url) > 3:
                return CustomRedirect(
                    redirect_url + '?token_valid=True&message=Credentials Valid&uidb64=' + uidb64 + '&token=' + token)
            else:
                return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return CustomRedirect(redirect_url + '?token_valid=False')

            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)
