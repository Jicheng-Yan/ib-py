#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Loops(object):
    """ generated source for Loops

    """

    @classmethod
    def main(cls, args):
        ## for-while
        a = 1
        while a < 10:
            a += 3
            print a
        ## for-while
        b = 0
        while b < 20:
            b += 2
        cls.doWhile()

    @classmethod
    def doWhile(cls):
        x = 0
        while True:
            print x
            x += 1
            if not x <= 10:
                break
        return x

if __name__ == '__main__':
    import sys
    Loops.main(sys.argv)

