# -*- coding: utf-8 -*-
from django.utils import translation
from django.conf import settings
import djclick as click
from contacts import jp, models, serializers
from logging import getLogger
log = getLogger()

translation.activate(settings.LANGUAGE_CODE)
JP_URL = 'http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip'


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.option('--url', '-u', default=JP_URL, help='URL')
@click.option('--cache', '-c', is_flag=True)
@click.pass_context
def column_length(ctx, url, cache):
    '''column length'''
    length = {}
    for i, row, errors in jp.open_csv(url=url, cache=cache):
        for key, value in row.items():
            length[key] = max(len(value), length.get(key, 0))
    click.echo(length)


@main.command()
@click.option('--url', '-u', default=JP_URL, help='URL')
@click.option('--cache', '-c', is_flag=True)
@click.pass_context
def reload_address(ctx, url, cache):
    '''reload address table'''

    models.Address.objects.all().delete()
    for i, row, errors in jp.open_csv(url=url, cache=cache):
        row['prefecture_ptr'] = models.Prefecture.filter(
            name=row.get('prefecture', '')).first()
        models.Address.objects.create(**row)


@main.command()
@click.pass_context
def init_prefecture(ctx):
    '''Initialize Prefecture'''
    from corekit.defs import PREFECTURES
    from contacts.models import Prefecture, Address
    map(lambda i: Prefecture.objects.get_or_create(name=i), PREFECTURES)
    for i in Address.objects.filter(prefecture_ptr__isnull=True):
        i.prefecture_ptr = Prefecture.objects.filter(name=i.prefecture).first()
        i.save()


@main.command()
@click.pass_context
def generate_json(ctx):
    '''generate json files'''
    for i in models.Address.objects.values_list('zipcode').distinct():
        zipcode = i[0]
        qs = models.Address.objects.filter(zipcode=zipcode)
        data = serializers.to_json_file(
            serializers.AddressSerializer(instance=qs, many=True).data)

        jsondata = models.AddressJson.objects.filter(zipcode=zipcode).first()
        if jsondata:
            jsondata.entries = qs.count()
            jsondata.data = data
            jsondata.save()
        else:
            models.AddressJson.objects.create(
                zipcode=zipcode, entries=qs.count(), data=data)
