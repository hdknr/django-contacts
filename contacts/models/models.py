from django.db import models
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
