class Base(object):
    """docstring for Base."""

    def __init__(self, id=0):
        super(Base, self).__init__()
        self.id = id

a = Base()
print(a)
