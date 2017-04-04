# coding: utf-8
from django.utils import six
from corekit.files import csvutils
from corekit.utils import contents
import requests
import zipfile
import os
from .defs import Address

JP_URL = 'http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip'
JP_FILE = 'KEN_ALL.CSV'


def download(url=JP_URL, cache=True, path='/tmp'):
    filename = os.path.join(path, JP_FILE)
    if not cache or not os.path.exists(filename):
        zipfile.ZipFile(
            contents(requests.get(url).content)).extractall(path=path)
    return filename


def open_csv(url=JP_URL, cache=True, path='/tmp'):
    filename = download(url=url, cache=cache, path=path)
    headers = [f.name for f in Address._meta.fields]
    return csvutils.CsvReader(open(filename), headers=headers)
