# coding: utf-8
from core.methods import CoreModel


class Address(CoreModel):

    def full_address(self, prefix=''):
        return u"{}{} {} {} {}".format(
            prefix, self.zipcode, self.prefecture, self.city, self.area)
