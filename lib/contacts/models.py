# coding: utf-8
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from corekit.defs import CoreModel
from . import defs, methods


class Prefecture(defs.Prefecture, CoreModel):

    class Meta:
        verbose_name = _('Prefecture')
        verbose_name_plural = _('Prefectures')
        ordering = ['-ordinal', 'id']

    def __unicode__(self):
        return self.name


class Address(defs.Address, CoreModel, methods.Address):
    prefecture_ptr = models.ForeignKey(
        Prefecture, verbose_name=_('Prefecture'),
        null=True, default=None, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __unicode__(self):
        return self.full_address()


class AddressJson(defs.AddressJson, CoreModel):

    class Meta:
        verbose_name = _('Address Json')
        verbose_name_plural = _('Addresses Json')
