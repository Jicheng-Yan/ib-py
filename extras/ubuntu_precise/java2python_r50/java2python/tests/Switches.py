#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Switches(object):
    """ generated source for Switches

    """

    @classmethod
    def main(cls, args):
        print cls.switches()

    @classmethod
    def switches(cls):
        i = 0
        i = 3
        if i in (1, 2):
            pass
        elif i == 3:
            i = 2
        else:
            return -4
        if False:
            pass
        else:
            i = 2
        return -1

if __name__ == '__main__':
    import sys
    Switches.main(sys.argv)

