#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ib.ext.cfg.EWrapperMsgGenerator -> config module for EWrapperMsgGenerator.java.

"""
modulePreamble = [
    'from ib.ext.AnyWrapperMsgGenerator import AnyWrapperMsgGenerator',
    'from ib.ext.Util import Util',
    'from ib.ext.TickType import TickType',
    'from ib.ext.EClientSocket import EClientSocket',
    ]

outputSubs = [
    (r'Double.MAX_VALUE', r"float('inf')"),
    (r'Math\.abs', r'abs'),
    (r'Double\.toString', r'str'),
    (r' \+ \" \(\" \+ DateFormat\.getDateTimeInstance\(\)\.format\(Date\(time \* 1000\)\) \+ \"\)\"', r''),
    ]


