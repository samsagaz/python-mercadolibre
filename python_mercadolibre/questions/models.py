class QuestionModel:
    def __init__(self, **kwargs):
        self.raw_data = dict(**kwargs)
        self.__dict__.update(kwargs)
