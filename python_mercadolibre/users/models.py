from collections import namedtuple

from python_mercadolibre.core.models.base import ModelBase

Address = namedtuple('Address', ["address", "city", "state", "zip_code"])
Phone = namedtuple("Phone", ["area_code", "extension", "number", "verified"])


class Profile(ModelBase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if hasattr(self, 'address'):
            self.address = Address(**self.address)
        if hasattr(self, 'phone'):
            self.phone = Phone(**self.phone)

    def __repr__(self):
        if hasattr(self, 'nickname'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.nickname)

        return super().__repr__()
