from django.contrib.auth import authenticate

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from identity.models import User
from apis.identity.permission import AdminPermission, UserPermission
from apis.identity.serializers import UserRegisterSerializer, AuthTokenSerializer, ProfileUpdateSerializer


class UserLoginView(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('emailId')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response(data={"message": "Invalid email or password"},
                            status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'access_token': token.key,
                         "userId": user.id,
                         "userFirstName": user.first_name,
                         "userLastName": user.last_name,
                         "userEmail": user.email,
                         "is_staff": user.is_superuser,
                         "message": "Login Successfully",},
                        status=status.HTTP_200_OK)


class UserCreationView(viewsets.ModelViewSet):
    permission_classes = (AdminPermission, )
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User(first_name=serializer.data.get('first_name'),
                    last_name=serializer.data.get('last_name'),
                    email=serializer.data.get('emailId'),
                   )
        user.set_password(serializer.data.get('password'))
        user.save()

        return Response(data={'response': {},
                              'message': 'Registration completed',
                             },
                        status=status.HTTP_200_OK)


class ProfileUpdateView(viewsets.ModelViewSet):
    permission_classes = (UserPermission, )
    http_method_names = ['put']
    queryset = User.objects.all()
    serializer_class = ProfileUpdateSerializer

