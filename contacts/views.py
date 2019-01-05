from django.shortcuts import render
from django.template import loader, engines
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from . import models


def render_by(name, request=None, **context):
    return mark_safe(
        loader.get_template(name).render(context, request=request))


def render(src, request=None, engine='django', **context):
    engine = engines[engine]
    request = request or None
    return mark_safe(
        engine.from_string(src).render(context, request=request))


def outbound_send(request, id):
    instance = models.Outbound.objects.filter(id=id).first() 
    if instance.poc == 'letter':
        return HttpResponse(
            render(instance.template, request=request, instance=instance))