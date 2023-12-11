"""
:author: Alexander Smyrnov
>>> w1 = BritishWeight(13)
>>> w2 = BritishWeight(1)
>>> w3 = BritishWeight(-5)
Traceback (most recent call last):
    ...
ArithmeticError: Ein Gewicht kann nicht negativ sein
>>> print(w1)
0 st 13 lb
>>> print(w2)
0 st 1 lb
>>> repr(w1)
'BritishWeight(13)'
>>> repr(w2)
'BritishWeight(1)'
>>> print(w1+w2)
1 st 0 lb
"""


class BritishWeight:
    """
    Klasse für britische Gewichter
    """

    def __init__(self, pounds=0):
        if pounds < 0:
            raise ArithmeticError("Ein Gewicht kann nicht negativ sein")
        self.pounds = pounds

    def __str__(self):
        stones = self.pounds // 14
        pounds = self.pounds % 14
        return f"{stones} st {pounds} lb"

    def __repr__(self):
        return f"BritishWeight({self.pounds})"

    def __add__(self, other):
        if isinstance(other, BritishWeight):
            pounds = self.pounds + other.pounds
            return BritishWeight(pounds)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BritishWeight):
            return self.pounds == other.pounds
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BritishWeight):
            return self.pounds < other.pounds
        return NotImplemented
