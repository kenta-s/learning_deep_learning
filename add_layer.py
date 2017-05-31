class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y

        return out

    def backward(self, dout):
        dx = 1 * dout
        dy = 1 * dout

        return dx, dy
