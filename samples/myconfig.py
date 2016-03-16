DEFINITIONS = {
    'BILIBILI' : 'com.typcn.Bilibili',
    'XEE'      : 'cx.c3.Xee3',
    'KINDLE'   : 'com.amazon.Kindle',
    'DeviceVendor::CHERRY': '0x046a',
    'DeviceProduct::3494' : '0x0011',
    '{{EMACS_IGNORE_APP}}': ['ECLIPSE', 'EMACS', 'TERMINAL',
                             'REMOTEDESKTOPCONNECTION', 'VI', 'X11',
                             'VIRTUALMACHINE', 'TERMINAL', 'SUBLIMETEXT'],
    'Open::ITERM'      : 'iTerm.app',
    'Open::FINDER'     : 'Finder.app',
    'Open::CHROME'     : 'Google Chrome.app',
    'Open::SUBLIME'    : 'Sublime Text.app',
    'Open::MONITOR'    : 'Activity Monitor.app',
    'Open::PREFERENCES': 'System Preferences.app',
    # Define a specifical key, the script will execute when pressed this key
    'Open::COPY_FINDER_PATH': '#! osascript /usr/local/bin/copy_finder_path'
}

REMAPS = [
    ['(holding)' , 'esc'          , 'cmd_r ctrl_r alt_r shift_r'],
    ['(double)'  , 'fn'           , 'F12'],
    ['(double)'  , 'fn'           , 'cmd alt I', ['GOOGLE_CHROME']],
    ['(double)'  , 'brightness_up', 'Open::COPY_FINDER_PATH', 'F2'],

    ['brightness_down'   , 'F1'],
    ['dashboard'         , 'F3'],
    ['mission_control'   , 'F3'],
    ['launchpad'         , 'F4'],
    ['keyboardlight_low' , 'brightness_down'],
    ['keyboardlight_high', 'brightness_up'],

    ['alt A'       , 'Open::ITERM'],
    ['alt E'       , 'Open::FINDER'],
    ['alt C'       , 'Open::CHROME'],
    ['alt S'       , 'Open::SUBLIME'],
    ['ctrl cmd del', 'Open::MONITOR'],
    ['ctrl cmd ,'  , 'Open::PREFERENCES'],

    ['alt', 'cmd', ['CHERRY', '3494']],
    ['cmd', 'alt', ['CHERRY', '3494']],

    ['cmd K', 'up '   * 6          , ['SKIM']],
    ['cmd J', 'down ' * 6          , ['SKIM']],
    ['alt L', 'ctrl_r tab'         , ['SKIM']],
    ['alt H', 'ctrl_r shift_r tab' , ['SKIM']],

    ['cmd K', 'up '   * 30         , ['GOOGLE_CHROME']],
    ['cmd J', 'down ' * 30         , ['GOOGLE_CHROME']],
    ['alt L', 'ctrl_r tab'         , ['GOOGLE_CHROME']],
    ['alt H', 'ctrl_r shift_r tab' , ['GOOGLE_CHROME']],
    ['ctrl l', 'cmd_r l'           , ['GOOGLE_CHROME']],

    ['ctrl P'      , 'up '   * 6 , ['SKIM']],
    ['ctrl N'      , 'down ' * 6 , ['SKIM']],
    ['alt shift ,' , 'fn left'   , ['SKIM']],
    ['alt shift .' , 'fn right'  , ['SKIM']],

    ['ctrl D' , 'cmd_r del'   , ['XEE']],
    ['ctrl P' , 'cmd_r left'  , ['XEE']],
    ['ctrl N' , 'cmd_r right' , ['XEE']],

    ['alt shift ,' , 'alt_r up'   , ['FINDER']],
    ['alt shift .' , 'alt_r down' , ['FINDER']],

    ['alt shift ,' , 'cmd_r up'   , ['SUBLIMETEXT']],
    ['alt shift .' , 'cmd_r down' , ['SUBLIMETEXT']],
    ['ctrl P'      , 'up'         , ['SUBLIMETEXT']],
    ['ctrl N'      , 'down'       , ['SUBLIMETEXT']],

    ['ctrl P' , 'up'   , ['!{{EMACS_IGNORE_APP}}', '!SKIM', '!XEE']],
    ['ctrl N' , 'down' , ['!{{EMACS_IGNORE_APP}}', '!SKIM', '!XEE']],
    ['ctrl D' , 'fdel' , ['!{{EMACS_IGNORE_APP}}', '!SKIM', '!XEE']],

    ['alt shift ,' , 'cmd_r up'   , ['!{{EMACS_IGNORE_APP}}', '!SKIM', '!FINDER', '!SUBLIMETEXT']],
    ['alt shift .' , 'cmd_r down' , ['!{{EMACS_IGNORE_APP}}', '!SKIM', '!FINDER', '!SUBLIMETEXT']],

    ['ctrl B' , 'left'        , ['!{{EMACS_IGNORE_APP}}']],
    ['ctrl F' , 'right'       , ['!{{EMACS_IGNORE_APP}}']],
    ['alt B'  , 'alt_r left'  , ['!{{EMACS_IGNORE_APP}}']],
    ['alt F'  , 'alt_r right' , ['!{{EMACS_IGNORE_APP}}']],
    ['ctrl A' , 'cmd_r left'  , ['!{{EMACS_IGNORE_APP}}']],
    ['ctrl E' , 'cmd_r right' , ['!{{EMACS_IGNORE_APP}}']],
    ['ctrl H' , 'del'         , ['!{{EMACS_IGNORE_APP}}']],
    ['alt D'  , 'alt_r fdel'  , ['!{{EMACS_IGNORE_APP}}']],
    ['ctrl U' , 'cmd_r right cmd_r shift_r left del del norepeat', ['!{{EMACS_IGNORE_APP}}']],

    ['ctrl cmd F' , 'cmd_r return'                   , ['TERMINAL']],
    ['ctrl cmd F' , 'cmd_r shift_r F cmd_r shift_r -', ['SKIM', 'KINDLE']],
    ['ctrl cmd F' , 'cmd F'                          , ['VIRTUALMACHINE']],

    ['alt R' , 'cmd_r R' , ['VIRTUALMACHINE', 'X11']],
    ['alt E' , 'cmd_r E' , ['VIRTUALMACHINE', 'X11']],
    ['cmd D' , 'cmd_r D' , ['VIRTUALMACHINE', 'X11']],

    ['ctrl H'  , 'del'                               , ['VIRTUALMACHINE', 'X11']],
    ['ctrl D'  , 'fdel'                              , ['VIRTUALMACHINE', 'X11']],
    ['ctrl U'  , 'end shift home del del norepeat'   , ['VIRTUALMACHINE', 'X11']],

    ['ctrl alt del' , 'ctrl_r del'   , ['VIRTUALMACHINE', 'X11']],
    ['ctrl alt D'   , 'ctrl_r fdel'  , ['VIRTUALMACHINE', 'X11']],
    ['ctrl alt F'   , 'ctrl_r right' , ['VIRTUALMACHINE', 'X11']],
    ['ctrl alt B'   , 'ctrl_r left'  , ['VIRTUALMACHINE', 'X11']],

    ['cmd Q'     , 'alt_r F4'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd R'     , 'ctrl_r R'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd L'     , 'ctrl_r L'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd C'     , 'ctrl_r C'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd V'     , 'ctrl_r V'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd X'     , 'ctrl_r X'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd Z'     , 'ctrl_r Z'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd A'     , 'ctrl_r A'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd F'     , 'ctrl_r F'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd S'     , 'ctrl_r S'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd W'     , 'ctrl_r W'     , ['VIRTUALMACHINE', 'X11']],
    ['cmd T'     , 'ctrl_r T'     , ['VIRTUALMACHINE', 'X11']],
    ['ctrl A'    , 'home'         , ['VIRTUALMACHINE', 'X11']],
    ['cmd left'  , 'home'         , ['VIRTUALMACHINE', 'X11']],
    ['ctrl E'    , 'end'          , ['VIRTUALMACHINE', 'X11']],
    ['cmd right' , 'end'          , ['VIRTUALMACHINE', 'X11']],
    ['ctrl P'    , 'up'           , ['VIRTUALMACHINE', 'X11']],
    ['ctrl N'    , 'down'         , ['VIRTUALMACHINE', 'X11']],
    ['ctrl F'    , 'right'        , ['VIRTUALMACHINE', 'X11']],
    ['ctrl B'    , 'left'         , ['VIRTUALMACHINE', 'X11']],

    ['ctrl shift tab', 'cmd_r alt_r left', ['BILIBILI']],
    ['ctrl shift tab', 'cmd_r alt_r left', ['BILIBILI']],

    ['left' , 'cmd_r left' , ['XEE']],
    ['up'   , 'cmd_r left' , ['XEE']],
    ['H'    , 'cmd_r left' , ['XEE']],
    ['K'    , 'cmd_r left' , ['XEE']],
    ['right', 'cmd_r right', ['XEE']],
    ['down' , 'cmd_r right', ['XEE']],
    ['J'    , 'cmd_r right', ['XEE']],
    ['L'    , 'cmd_r right', ['XEE']],

    ['cmd P', 'cmd_r alt_r G', ['SKIM']],
]