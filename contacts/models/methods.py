from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _


class Contact(object):

    @cached_property
    def full_name(self):
        return f"{self.family_name}  {self.first_name}"

    @cached_property
    def address(self):
        return f"{self.prefecture}{self.city}{self.town}"