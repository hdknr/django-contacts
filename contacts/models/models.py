from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from . import defs


class Contact(defs.Contact):

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return f"{self.family_name} {self.first_name}"


class Family(defs.Family):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Family')
        verbose_name_plural = _('Families')
        ordering = ['contact', 'ordinal']

    def __str__(self):
        return f"{self.family_name} {self.first_name}"


class Outbound(defs.Outbound):
    owner = models.ForeignKey(
        User, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    contact_from = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Outbound')
        verbose_name_plural = _('Outbounds')

    def __str__(self):
        return f"{self.title}"


class OutboundTo(defs.OutboundTo):
    outbound = models.ForeignKey(Outbound, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Outbound To')
        verbose_name_plural = _('Outbound Tos')

    def __str__(self):
        return f"{self.contact}"