from collections import namedtuple

Address = namedtuple('Address', ["address", "city", "state", "zip_code"])
Phone = namedtuple("Phone", ["area_code", "extension", "number", "verified"])


class Profile:
    def __init__(self, **kwargs):
        self.raw_data = dict(**kwargs)
        self.__dict__.update(kwargs)
        if hasattr(self, 'address'):
            self.address = Address(**self.address)
        if hasattr(self, 'phone'):
            self.phone = Phone(**self.phone)

    def __eq__(self, other):
        if isinstance(other, Profile):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

    def __repr__(self):
        if hasattr(self, 'nickname'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.nickname)

        return super().__repr__()
