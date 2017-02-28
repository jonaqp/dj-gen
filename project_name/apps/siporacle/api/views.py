# coding=utf-8
from rest_framework.response import Response
from rest_framework.views import APIView

from project_name.apps.siporacle.models import (
    TS_INV_TM_USUARIOS
)
from .serializers import (
    TM_USUARIOSerializer
)


class SolicitanteAPIView(APIView):
    def get_object(self, pk):
        try:
            return TS_INV_TM_USUARIOS.objects.using('sip_oracle').get(pk=pk)
        except TS_INV_TM_USUARIOS.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        solicitante_id = self.get_object(pk)
        serializer = TM_USUARIOSerializer(solicitante_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        solicitante_id = self.get_object(pk)
        serializer = TM_USUARIOSerializer(solicitante_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolicitanteAPIListView(APIView):
    def get(self, request, format=None):
        solicitante = TS_INV_TM_USUARIOS.objects.using('sip_oracle').all()
        serializer = TM_USUARIOSerializer(solicitante, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TM_USUARIOSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
