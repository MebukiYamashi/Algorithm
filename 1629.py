import sys
A, B, C = map(int, sys.stdin.readline().split())
print(pow(A, B, C))

"""
time limit : 500ms, usable to sys.stdin.readline and pow for reduce runtime
pow(x, y[, z])
Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z). 
The two-argument form pow(x, y) is equivalent to using the power operator: x**y.
same as x ^ y [, %z]

"""