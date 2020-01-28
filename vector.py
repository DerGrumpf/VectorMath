class Vector(object):
    """docstring for Vector."""

    def __init__(self, *args):
        super(Vector, self).__init__()
        self.values = list(args)

    def __add__(self, vec):
        if type(vec) == type(self):
            if len(vec) == len(self):
                return Vector(*[sum(el) for el in zip(self, vec)])

            raise ValueError("Vectors must have the same Dimension")

        else:
            return Vector(*[vec+val for val in self])


    def __sub__(self, vec):
        return self + -vec

    def __mul__(self, vec):
        if type(vec) == type(self):
            if len(vec) == len(self):
                return Vector(*[v1*v2 for v1,v2 in zip(self, vec)])

            raise ValueError("Vectors must have the same Dimension")

        else:
            return Vector(*[vec*val for val in self])

    def __div__(self, vec):
        # This must be fixed
        raise ValueError("Division not defined")

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def __neg__(self):
        return Vector(*[-val for val in self])

    def __iter__(self):
        for val in self.values:
            yield val

if __name__ == '__main__':
    v = Vector(*[i**2 for i in range(10)])
    u = Vector(*[i**3 for i in range(-5,5)])

    print("Quadrtic Numbers (0..9)^2 V:", v)
    print("Cubic Numbers (-5..5)^2 U:", u)
    print("Addition V+U:", v+u)
    print("Addition V+2:", v+2)
    print("Subtraction V-U:", v-u)
    print("Subtraction U-2", u-2)
    print("Negation -V:", -v)
    print("Multiplication V*U:", v*u)
    print()

    try:
        v / u
    except Exception as e:
        print("Division Error Test: V/U")
        print("Exception:", e)

    print()

    d = Vector(*[i for i in range(5)])
    print("Vector D with Dimension 5:", d)
    try:
        d + v
    except Exception as e:
        print("Vector Dimension Error Test: D")
        print("Exception:", e)
