# coding: utf-8
from core import admin as core_admin


class AddressAdmin(core_admin.CoreAdmin):
    list_filter = ['prefecture_ptr', 'spans', 'street', 'shared', 'tiny', ]
    list_excludes = ['reason', 'updates', 'prefecture_ptr', ]
    search_fields = [
        'zipcode',
        'prefecture', 'city', 'area',
        'prefecture_kana', 'city_kana', 'area_kana', ]


core_admin.register(__name__, globals(), [],)
