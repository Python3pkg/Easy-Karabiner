# -*- coding: utf-8 -*-

import sys
import codecs

__all__ = ['ensure_utf8', 'u', 'write_utf8_to', 'is_string_type']


# if python 3.x
if sys.version_info[0] == 2:
    def write_utf8_to(s, outpath):
        with codecs.open(outpath, 'w', encoding='utf8') as fp:
            fp.write(s)
else:
    str = str
    str = str

    def write_utf8_to(s, outpath):
        with open(outpath, 'w') as fp:
            fp.write(s)


def is_string_type(s):
    return isinstance(s, str)


def ensure_utf8(s):
    # convert from any object to `unicode`
    if not isinstance(s, str):
        s = str(s)

    if isinstance(s, str):
        s = s.encode('utf-8')
    return str(s, encoding='utf-8')


u = ensure_utf8
