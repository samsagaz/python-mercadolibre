from collections import namedtuple

Answer = namedtuple("Answer", ["text", "status", "date_created"])
FromCustomer = namedtuple("From", ["id", "answered_questions"])


class QuestionModel:
    def __init__(self, **kwargs):
        self.raw_data = dict(**kwargs)
        if 'from' in kwargs:
            kwargs['from_customer'] = kwargs.pop('from')
        self.__dict__.update(kwargs)
        if hasattr(self, 'from_customer'):
            self.from_customer = FromCustomer(**self.from_customer)
        if hasattr(self, 'answer'):
            self.answer = Answer(**self.answer)

    def __eq__(self, other):
        if isinstance(other, QuestionModel):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class QuestionPostModel:
    def __init__(self, **kwargs):
        self.raw_data = dict(**kwargs)
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, QuestionModel):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented
