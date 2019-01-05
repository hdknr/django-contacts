from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from . import methods


class Timestamp(models.Model):
    created_at = models.DateTimeField(_('Created At'), default=now) 
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        abstract = True


class BasePerson(models.Model):
    family_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    first_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    family_name_kana = models.CharField(max_length=50, null=True, blank=True, default=None)
    first_name_kana = models.CharField(max_length=50, null=True, blank=True, default=None) 

    birth_date = models.DateField(null=True, blank=True, default=None)
    gender = models.CharField(max_length=10, null=True, blank=True, default=None)

    class Meta:
        abstract = True


class BaseAddress(models.Model):

    postal_code = models.CharField(max_length=10)
    prefecture = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    building = models.CharField(max_length=50, null=True, blank=True, default=None)

    class Meta:
        abstract = True


class BaseProfession(models.Model):

    company = models.CharField(max_length=50, null=True, blank=True, default=None)
    job_title = models.CharField(max_length=10, null=True, blank=True, default=None)

    class Meta:
        abstract = True


class BasePoc(models.Model):

    phone = models.CharField(max_length=20, null=True, blank=True, default=None)
    email = models.EmailField(null=True, blank=True, default=None)
    url = models.URLField(null=True, blank=True, default=None)

    class Meta:
        abstract = True


class Contact(BasePerson, BaseAddress, BaseProfession, BasePoc, Timestamp, methods.Contact):

    class Meta:
        abstract = True


class Family(BasePerson, Timestamp):
    role = models.CharField(max_length=50, null=True, blank=True, default=None)
    suffix = models.CharField(max_length=50, null=True, blank=True, default=None)
    ordinal = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Outbound(Timestamp):
    title = models.CharField(max_length=100)
    poc = models.CharField(max_length=50)
    template = models.TextField(null=True, blank=True, default=None)

    class Meta:
        abstract = True


class OutboundTo(Timestamp):
    closed = models.BooleanField(default=False)
    closed_at = models.DateTimeField(_('Closed At'), null=True, default=None, blank=True)

    class Meta:
        abstract = True