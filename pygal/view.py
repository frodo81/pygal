class Margin(object):
    def __init__(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    @property
    def x(self):
        return self.left + self.right

    @property
    def y(self):
        return self.top + self.bottom


class Box(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class View(object):
    def __init__(self, width, height, xmin, xmax, ymin, ymax):
        self.width = width
        self.height = height
        xrng = (xmax - xmin) or 1
        yrng = (ymax - ymin) or 1
        if (ymax - ymin) == 0:
            ymin -= .5
        self.box = Box(xmin, ymin, xrng, yrng)

    def x(self, x):
        return self.width * (x - self.box.x) / float(self.box.width)

    def y(self, y):
        return (self.height - self.height *
                (y - self.box.y) / float(self.box.height))

    def __call__(self, xy):
        x, y = xy
        return (self.x(x), self.y(y))
