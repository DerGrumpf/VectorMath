from vector import Vector

v = Vector(*[i**2 for i in range(10)])
u = Vector(*[i**3 for i in range(-5,5)])

print("Quadrtic Numbers (0..9)^2 V:", v)
print("Reversed:", reversed(v))
print("Cubic Numbers (-5..5)^3 U:", u)
print("Addition V+U:", v+u)
print("Addition V+2:", v+2)
print("Subtraction V-U:", v-u)
print("Subtraction U-2.", u-2)
print("Negation -V:", -v)
print("Multiplication V*U:", v*u)
print("Power V^3:", v**3)
print("Access 3th item V[3]:", v[3])
print("Bool Check for V:", bool(v))
print("Dotproduct <V,U>:", v.dotproduct(u))
print("Magnitude ||V||:", v.magnitude())
print()

try:
    v / u
except Exception as e:
    print("Division Error Test: V/U")
    print("Exception:", e)

print()

d = Vector(*[i for i in range(5)])
print("Vector D with Dimension", len(d), ":", d)
try:
    d + v
except Exception as e:
    print("Vector Dimension Error Test: D")
    print("Exception:", e)
