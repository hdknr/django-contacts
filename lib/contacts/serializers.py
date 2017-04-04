# coding: utf-8
from corekit.serializers import BaseModelSerializer, BaseObjectSerializer
from . import models


class AddressSerializer(BaseModelSerializer):

    class Meta:
        model = models.Address
        fields = ['zipcode', 'prefecture', 'city', 'area', ]


to_json = BaseObjectSerializer.to_json
to_json_file = BaseObjectSerializer.to_json_file
