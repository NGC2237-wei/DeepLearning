# 包装numpy数组 做初始化
class Parameter(object):
    def __init__(self, data, requires_grad):
        self.data = data
        self.grad = None
        self.requires_grad = requires_grad

    @property
    def T(self):
        return self.data.T
