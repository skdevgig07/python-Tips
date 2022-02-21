class Maybe(object):
    def __init__(self, val, error=None):
        self.val = val
        self.error = error

    def __repr__(self):
        if self.val is not None:
            return repr(self.val)
        else:
            return repr(self.error)

    def do(self, func):
        if self.val is None:
            return self
        try:
            return Maybe(func(self.val))
        except Exception as e:
            return Maybe(None, e)

def squared(x):
    return x * x

def addone(x):
    return x + 1

result1 = Maybe(5).do(squared).do(addone)
result2 = Maybe('a').do(squared).do(addone)
print result1
print result2
