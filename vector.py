from math import sqrt

class Vector(object):
    """Defines a interactive usable Vector class"""

    version = 0.1

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

    def __truediv__(self, vec):
        raise ValueError("Division not defined")

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self)

    def __len__(self):
        '''Returns Dimension of this Vector'''
        return len(self.values)

    def __neg__(self):
        return Vector(*[-val for val in self])

    def __pos__(self):
        return self

    def __iter__(self):
        for val in self.values:
            yield val

    def __iadd__(self, vec):
        return self + vec

    def __isub__(self, vec):
        return self - vec

    def __imul__(self, vec):
        return self * vec

    def __itruediv__(self, vec):
        # same as __div__
        return self / vec

    def __pow__(self, scalar):
        '''raise Matrix Values to a given Power Value'''
        if scalar > 0:
            v = Vector(*self)
            for _ in range(scalar):
                v *= v
            return v

        if scalar < 0:
            pass

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __reversed__(self):
        return Vector(*[val for val in reversed(self.values)])

    def __bool__(self):
        return not len(self) == 0


    # After here functions must be define

    def dotproduct(self, vec):
        if not len(self) == len(vec):
            raise ValueError("Vectors must have the same Dimension")
        return sum(self*vec)

    def crossproduct(self, vec):
        pass

    def tripleproduct(self, vec1, vec2):
        raise NotImplementedError("Tripleproduct WIP")
        return (self.crossproduct(vec1)).dotproduct(vec2)

    def magnitude(self):
        '''Returns length of the Vector'''
        return sqrt(self.dotproduct(self))

    def sqrt_magnitude(self):
        '''Returns length of the Vector squared'''
        return self.dotproduct(self)

    def norm(self):
        '''Returns this normalized Vector with length 1'''
        pass

class Vector3(Vector):
        back = None
        down = None
        forward = None
        left = None
        one = None
        right = None
        up = None
        zero = None

class Vector2(Vector):
        back = None
        down = None
        forward = None
        left = None
        one = None
        right = None
        up = None
        zero = None
