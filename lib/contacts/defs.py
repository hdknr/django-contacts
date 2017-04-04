# coding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .files import AddressJsonPath


class Address(models.Model):
    code = models.CharField(_('JIS Code'), max_length=10)
    zipcode5 = models.CharField(_('Zipcode 5'), max_length=5)
    zipcode = models.CharField(
        _('Zipcode'), max_length=7, db_index=True)

    prefecture_kana = models.CharField(
        _('Prefecture Kana'), max_length=10, db_index=True)
    city_kana = models.CharField(_('City Kana'), max_length=30, db_index=True)
    area_kana = models.CharField(_('Area Kana'), max_length=100, db_index=True)

    prefecture = models.CharField(_('Prefecture'), max_length=10, db_index=True)
    city = models.CharField(_('City'), max_length=30, db_index=True)
    area = models.CharField(_('Area'), max_length=100, db_index=True)

    spans = models.PositiveSmallIntegerField(_('Spans Entries'))
    tiny = models.PositiveSmallIntegerField(_('Tiny Town'))
    street = models.PositiveSmallIntegerField(_('Has Street'))
    shared = models.PositiveSmallIntegerField(_('Shared Zipcode'))
    updates = models.PositiveSmallIntegerField(_('Updates'))
    reason = models.PositiveSmallIntegerField(_('Reason'))

    class Meta:
        abstract = True


class AddressJson(models.Model):
    zipcode = models.CharField(
        _('Zipcode'), max_length=7, db_index=True, unique=True)
    entries = models.PositiveSmallIntegerField(_('Address Entries'), default=1)
    data = models.FileField(
        _('Address Json File'), upload_to=AddressJsonPath('public', 'data',))

    class Meta:
        abstract = True


class Prefecture(models.Model):
    name = models.CharField(_('Prefecture Name'), max_length=10, db_index=True)

    class Meta:
        abstract = True
