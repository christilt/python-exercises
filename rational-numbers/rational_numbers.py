from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        if (denom < 0):
            numer *= -1
            denom *= -1
        self.__gcd = gcd(numer, denom)
        self.numer = numer // self.__gcd
        self.denom = denom // self.__gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = int(self.numer * other.denom + other.numer * self.denom)
        denom = int(self.denom * other.denom)
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = int(self.numer * other.denom - other.numer * self.denom)
        denom = int(self.denom * other.denom)
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = int(self.numer * other.numer)
        denom = int(self.denom * other.denom)
        return Rational(numer, denom)

    def __truediv__(self, other):
        denom = int(other.numer * self.denom)
        if denom == 0:
            raise ZeroDivisionError
        numer = int(self.numer * other.denom)
        return Rational(numer, denom)

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

    def __pow__(self, power):
        numer = pow(self.numer, power)
        denom = pow(self.denom, power)
        return Rational(numer, denom)

    def __rpow__(self, base):
        p = pow(base, self.numer)
        q = self.denom
        return self.__root(p, q)

    def __root(self, p, q):
        """ root(p, q) is the qth root of p """
        return p**(1/float(q))