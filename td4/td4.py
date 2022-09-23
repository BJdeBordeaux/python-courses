from abc import ABC, abstractmethod
import sys

print("hello world")


class Rope(ABC):
    def __init__(self, d):
        self.length = 0

    @abstractmethod
    def __getitem__(self, i):
        pass

    @abstractmethod
    def __add__(self, r):
        pass

    @abstractmethod
    def __str__(self):
        pass


class App(Rope):  # Node with left and Right
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __getitem__(self, i):
        if isinstance(i, int):
            if i <= self.left.size():
                return self.left.__getitem__(i)
            else:
                return self.right.__getitem__(i - self.left.size())
        elif isinstance(i, slice):
            if i.step is None:
                step = 1
            else:
                step = i.step
            if i.start is None:
                start = 0
            else:
                start = i.start
            if i.stop is None:
                stop = self.size()
            else:
                stop = i.stop
            if start < 0:
                start = self.size() + start
            if stop < 0:
                stop = self.size() + stop
            if start > stop:
                return ""
            if step > 0:
                if start >= self.left.size():
                    return self.right.__getitem__(
                        slice(start - self.left.size(), stop - self.left.size(), step)
                    )
                elif stop <= self.left.size():
                    return self.left.__getitem__(slice(start, stop, step))
                else:
                    return self.left.__getitem__(
                        slice(start, self.left.size(), step)
                    ) + self.right.__getitem__(slice(0, stop - self.left.size(), step))
            else:
                if start >= self.left.size():
                    return self.right.__getitem__(
                        slice(start - self.left.size(), stop - self.left.size(), step)
                    )
                elif stop <= self.left.size():
                    return self.left.__getitem__(slice(start, stop, step))
                else:
                    return self.right.__getitem__(
                        slice(self.right.size() - 1, self.right.size() - stop - 1, step)
                    ) + self.left.__getitem__(
                        slice(self.left.size() - 1, self.left.size() - start - 1, step)
                    )

    def __add__(self, r):
        rightmost_parent = self.rightmostparent()
        # print("self = {}, left = {}, right = {}".format(self, self.left, self.right))
        if rightmost_parent.right.size() + r.size() <= 10:
            # print("change rightmost: {} + {}".format(rightmost_parent.right, r))
            rightmost_parent.right += r
            return self
        else:
            # print("new app")
            return App(self, r)

    def __str__(self):
        return self.left.__str__() + self.right.__str__()

    def size(self):
        return self.left.size() + self.right.size()

    def rightmostparent(self):
        if isinstance(self.right, App):
            return rightmostparent(self.right)
        else:
            return self


class Str(Rope):  # Node with a string
    def __init__(self, s):
        self.s = s

    def __getitem__(self, i):
        return self.s[i]

    def __add__(self, r):
        # print("self = {}, r = {}".format(self, r))
        if self.size() + r.size() <= 10:
            # print("concat str")
            return Str(self.s + r.s)
        else:
            # print("str new app")
            return App(self, r)

    def __str__(self):
        return self.s

    def size(self):
        return len(self.s)


testStr = Str("Hello")
assert(testStr[0] == "H")
assert(testStr[1:] == "ello")
assert(testStr[1:3] == "el")
assert(str(testStr + Str(testStr[0])) == "HelloH")

r = App(
    Str("La structure de"),
    App(
        App(Str("corde per"), Str("met de manipuler")),
        App(Str(" de grandes "), Str("chaînes")),
    ),
)
assert(str(r) == "La structure decorde permet de manipuler de grandes chaînes")
assert(r[6] == "u")
assert(r[16] == "o")
assert(str(r[21:54]) == "permet de manipuler de grandes ch")

assert(str(Str("chai") + Str("ne")) == "chaine")
assert(str((Str("debut de la ") + Str("chai") + Str("ne")).right) == "chaine")
