#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TryCatchTests(object):
    """ generated source for TryCatchTests

    """

    def tryCatchSimple(self):
        try:
            print "try block"
        except (Exception, ), e:
            print "catch Exception block"

    def tryCatchCompound(self):
        try:
            print "try block"
        except (RuntimeException, ), re:
            print "catch RuntimeException block"
        except (Exception, ), e:
            print "catch Exception block"

    def tryCatchThrowSimple(self):
        try:
            print "try block"
        except (Exception, ), e:
            print "catch Exception block"
            raise e

    def tryCatchThrowCompound(self):
        try:
            print "try block"
        except (RuntimeException, ), re:
            print "catch RuntimeException block"
            raise re
        except (Exception, ), e:
            print "catch Exception block"
            raise e


