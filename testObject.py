class testObject(object):
    """docstring for """
    def __init__(self, arg):
        # super(, self).__init__()
        self.arg = arg
    def get(self):
        return self.arg
    def set(self, arg):
        self.arg = arg
