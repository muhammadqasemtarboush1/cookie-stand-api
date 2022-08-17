from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieSerializer
from rest_framework import status


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStand
        exclude = ['owner']


class CookieList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer

    def post(self, request):
        es = EventSerializer(data=request.data)
        if es.is_valid():
            es.save(owner=self.request.user)

            return Response(status=status.HTTP_201_CREATED, data=es.data)
        return Response(data=es.errors, status=status.HTTP_400_BAD_REQUEST)


class CookieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer
