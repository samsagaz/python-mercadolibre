class Profile:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"<User(nickname={self.nickname!r})>"

    def __str__(self):
        return f"<User(nickname={self.nickname})>"
