# coding=utf-8
from rest_framework_json_api import serializers

from ..models import TS_INV_TM_USUARIOS


class TM_USUARIOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TS_INV_TM_USUARIOS
        exclude = []



