# coding: utf-8
from core import admin as core_admin


class AddressAdmin(core_admin.CoreAdmin):
    list_filter = ['prefecture_ptr', 'spans', 'street', 'shared', 'tiny', ]
    list_excludes = ['reason', 'updates', 'prefecture_ptr', ]


core_admin.register(__name__, globals(), [],)
