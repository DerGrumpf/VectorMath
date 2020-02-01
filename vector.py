from math import sqrt

class Vector(object):
    """Defines a interactive usable Vector class"""

    version = 0.1

    def __init__(self, *args) -> None:
        super(Vector, self).__init__()
        self.values = list(args) #should be a dict

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

    def __truediv__(self, vec) -> Exception:
        raise ValueError("Division not defined")

    def __str__(self) -> str:
        o = str()
        for i, v in enumerate(self):
            if i == len(self)-1:
                o += str(v)
            else:
                o += str(v) + ', '
        return o

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

class Vector4(Vector):

        one = Vector(1,1,1,1)
        zero = Vector(0,0,0,0)

        def __init__(self, x, y, z, w) -> None:
            super(Vector3, self).__init__(x,y,z,w)
            # this need to be bound with the values list
            self.x, self.y, self.z, self.w = x, y, z, w

class Vector3(Vector):
        back = Vector(0,0,-1)
        down = Vector(0,-1,0)
        forward = Vector(0,0,1)
        left = Vector(-1,0,0)
        one = Vector(1,1,1)
        right = Vector(1,0,0)
        up = Vector(0,1,0)
        zero = Vector(0,0,0)

        def __init__(self, x, y, z) -> None:
            super(Vector3, self).__init__(x,y,z)
            # this need to be bound with the values list
            self.x, self.y, self.z = x, y, z

class Vector2(Vector):
        down = Vector(0,-1)
        left = Vector(-1,0)
        one = Vector(1,1)
        right = Vector(1,0)
        up = Vector(0,1)
        zero = Vector(0,0)

        def __init__(self, x, y) -> None:
            super(Vector2, self).__init__(x,y)
            self.x, self.y = x, y
