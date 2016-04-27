# -*- coding: utf-8 -*-
from easy_karabiner.main import *


def test_main():
    def cmd(*args, **kwargs):
        try:
            main.callback(*args, **kwargs)
            return 0
        except SystemExit as e:
            return e.code

    inpath = 'samples/test.py'
    outpath = 'samples/test.xml'

    assert(cmd(inpath, outpath, verbose=True, string=True) == 0)
    assert(cmd(inpath, outpath, help=True) == 0)
    assert(cmd(inpath, outpath, reload=True) == 0)
    assert(cmd(inpath, outpath, version=True) == 0)
    assert(cmd(inpath, outpath, list_peripherals=True) == 0)
