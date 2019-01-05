from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .. import models


class FamilyInline(admin.StackedInline):
    model = models.Family
    exclude = ['created_at', ]
    readonly_fields = ['updated_at']
    classes = ['collapse']
    extra = 0


class OutboundToInline(admin.TabularInline):
    model = models.OutboundTo
    exclude = ['created_at', ]
    readonly_fields = ['updated_at']
    raw_id_fields = ['contact']
    extra = 0