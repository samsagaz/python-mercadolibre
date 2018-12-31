
class ModelBase:
    def __init__(self, **kwargs):
        self.raw_data = dict(**kwargs)
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, ModelBase):
            return self.__dict__ == other.__dict__

        return NotImplemented

    def __int__(self):
        if hasattr(self, 'id'):
            return self.id

        return self.NotImplemented
