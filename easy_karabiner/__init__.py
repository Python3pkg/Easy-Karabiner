__version__ = '0.5.0'


# Used for test purpose
if __name__ == '__main__':
    import sys
    from easy_karabiner.__main__ import *

    inpath = sys.argv[1]
    outpath = inpath + '.xml'

    try:
        print(inpath.center(80, '='))
        main.callback(inpath, outpath, verbose=True)
    except SystemExit as e:
        print(e.code)
