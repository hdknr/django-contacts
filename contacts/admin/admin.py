from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .. import models
from ..models import defs
from . import inlines


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'family_name', 'first_name', 
        'postal_code', 'prefecture', 'city', 'town', 
    ]
    exclude = ['created_at']
    readonly_fields = ['updated_at']
    inlines = [
        inlines.FamilyInline,
    ]
    fieldsets = (
        (_('Person'), {
            'classes': ('collapse',),
            'fields': [f.name for f in defs.BasePerson._meta.fields],
        }),
        (_('Address'), {
            'classes': ('collapse',),
            'fields': [f.name for f in defs.BaseAddress._meta.fields],
        }),
        (_('Profession'), {
            'classes': ('collapse',),
            'fields': [f.name for f in defs.BaseProfession._meta.fields],
        }),
        (_('Poc'), {
            'classes': ('collapse',),
            'fields': [f.name for f in defs.BasePoc._meta.fields],
        }),
    )


@admin.register(models.Outbound)
class Outbound(admin.ModelAdmin):
    list_display = [f.name for f in models.Outbound._meta.fields]
    exclude = ['created_at']
    readonly_fields = ['updated_at']
    raw_id_fields = ['contact_from', 'owner']
    inlines = [
        inlines.OutboundToInline,
    ]