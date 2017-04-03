from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WygConfig(AppConfig):
    name = 'wyg'
    verbose_name = _('Wyg')
