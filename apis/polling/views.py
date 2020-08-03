from django.db.models import Sum

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from identity.models import User
from polling.models import Polling
from apis.polling.serializers import CandidateListSerializer, PollingSerializer
from apis.polling.utils import get_client_ip


class CandidateListView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = User.objects.all()
    serializer_class = CandidateListSerializer


class BestCandidateView(APIView):

    def get(self, request):
        dataStrucure = Polling.objects.values('candidate__id').annotate(dataStrucure=Sum('data_structure')).\
            order_by('-dataStrucure')[:5]
        algorithm = Polling.objects.values('candidate__id').annotate(algorithm=Sum('algorithm')). \
            order_by('-algorithm')[:5]
        cplusplus = Polling.objects.values('candidate__id').annotate(cplusplus=Sum('cplusplus')). \
            order_by('-cplusplus')[:5]
        python = Polling.objects.values('candidate__id').annotate(python=Sum('python')). \
            order_by('-python')[:5]
        java = Polling.objects.values('candidate__id').annotate(java=Sum('java')). \
                     order_by('-java')[:5]

        return Response(data={"message": "best hacker",
                              "data": ""},
                        status=status.HTTP_200_OK
                        )


class PollingView(APIView):
    def post(self, request):
        serializer = PollingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(id=serializer.data.get('id'))
        ip = get_client_ip(request)
        if Polling.objects.filter(ip=ip, candidate=user).exitst():
            return Response(data={"message": "you are already voted"},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        Polling.objects.create(ip=ip, candidate=user, java=serializer.data.get('java'),
                               python = serializer.data.get('python'),
                               cplusplus = serializer.data.get('cplusplus'),
                               algorithm = serializer.data.get('algorithm'),
                               data_structure = serializer.data.get('data_structure'))
        return Response(data={"message": "you are already voted"},
                        status=status.HTTP_200_OK
                        )
