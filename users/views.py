import os
import random
import string

from django.core.mail import send_mail
from dotenv import load_dotenv
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination


from .models import Buffer, User
from .permissions import IsAdministrator
from .serializers import UserSerializer


def code_gen(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


load_dotenv()


@api_view(['POST'])
def send_code(request):
    email_from = os.getenv('EMAIL_HOST_USER')
    email_to = request.GET.get('email')
    code = code_gen()
    try:
        current_user = Buffer.objects.get(email=email_to)
        current_user.code = code
        current_user.save()
    except Buffer.DoesNotExist:
        Buffer.objects.create(email=email_to, code=code)
    send_mail(
        'Confirmation code',
        f'Your confirmation code: {code}',
        from_email=email_from,
        recipient_list=[email_to, ],
        fail_silently=False,
    )
    return Response({"email": email_to}, status=status.HTTP_200_OK)


@api_view(['POST'])
def send_token(request):
    try:
        request_email = request.GET.get('email')
        request_code = request.GET.get('confirmation_code')
        current_user = Buffer.objects.get(email=request_email)
    except Buffer.DoesNotExist:
        return Response({"error": "wrong email"}, status=status.HTTP_400_BAD_REQUEST)
    if request_code == current_user.code:
        try:
            new_user = User.objects.get(email=request_email)
        except User.DoesNotExist:
            serialized = UserSerializer(data=request.DATA)
            if serialized.is_valid():
                User.objects.create_user(**serialized.init_data)
        current_user.delete()
        refresh = RefreshToken.for_user(new_user)
        return Response({"token": str(refresh.access_token)}, status=status.HTTP_200_OK)
    return Response({"error": "wrong code"}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdministrator, permissions.IsAdminUser]
    pagination_class = PageNumberPagination

    @action(detail=False, permission_classes=(permissions.IsAuthenticated,),
            methods=['get', 'patch'], url_path='me')
    def get_or_update_self(self, request):
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(request.user, many=False)
            return Response(serializer.data)
