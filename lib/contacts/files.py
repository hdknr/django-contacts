# coding: utf-8
from __future__ import unicode_literals
from django.utils.deconstruct import deconstructible

from core.files import UploadPath
from logging import getLogger
logger = getLogger()


@deconstructible
class AddressJsonPath(UploadPath):

    def create_name(self, instance, filename):
        if filename:
            return u"{}.json".format(instance.zipcode)
