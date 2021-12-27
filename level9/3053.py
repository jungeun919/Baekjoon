import math

def euclid(r):
    return r * r * math.pi

def taxi(r):
    return r * r * 2

R = int(input())
print(euclid(R))
print(taxi(R))