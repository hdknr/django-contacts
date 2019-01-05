from django.apps import AppConfig as DjAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(DjAppConfig):
    name = 'contacts'
    verbose_name = _('Contacts')
