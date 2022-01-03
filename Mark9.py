class Constant(object):
    val = 0
    val+=1
    def __init__(self, val):
        super(Constant, self).__setattr__("value", val)
    def __setattr__(self, name, val):
        raise ValueError(self.val)

o1 = Constant()
o1.__init__()