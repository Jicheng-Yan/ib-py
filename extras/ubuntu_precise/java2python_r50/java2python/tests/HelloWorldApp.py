#!/usr/bin/env python
# -*- coding: utf-8 -*-


class HelloWorldApp(object):
    """ generated source for HelloWorldApp

    """

    def foo(self):
        print "FOO"

    @classmethod
    def main(cls, args):
        print "Hello, world."
        print args

if __name__ == '__main__':
    import sys
    HelloWorldApp.main(sys.argv)

