DEFINITIONS = {
    'cherry_3494': ['0x046a', '0x0011'],
    'emacs_ignore_app': ['ECLIPSE', 'EMACS', 'TERMINAL',
                         'REMOTEDESKTOPCONNECTION', 'VI', 'X11',
                         'VIRTUALMACHINE', 'TERMINAL', 'Sublime Text'],
}

MAPS = [
    ['__FlipScrollWheel__', 'flipscrollwheel_vertical', ['!APPLE_COMPUTER', '!ANY']],
    ['_holding_', 'esc', 'cmd_r ctrl_r alt_r shift_r'],
    ['_double_' , 'fn' , 'F12'],
    ['_double_' , 'fn' , 'cmd alt I', ['Google Chrome']],
    ['_press_modifier_', 'ctrl', 'esc'],

    ['alt mouse_left', 'mouse_left "#! osascript /usr/local/bin/copy_finder_path"'],

    ['F5', 'brightness_down', ['!PyCharm CE']],
    ['F6', 'brightness_up', ['!PyCharm CE']],
    ['F10', 'volume_mute', ['!PyCharm CE']],
    ['F11', 'volume_down', ['!PyCharm CE']],
    ['F12', 'volume_up', ['!PyCharm CE']],

    ['alt A'       , 'iTerm'],
    ['alt E'       , 'Finder'],
    ['alt C'       , 'Google Chrome'],
    ['alt S'       , 'Sublime Text'],
    ['alt P'       , 'PyCharm CE'],
    ['ctrl cmd del', 'Activity Monitor'],
    ['ctrl cmd ,'  , 'System Preferences'],

    ['alt', 'cmd', ['cherry_3494']],
    ['cmd', 'alt', ['cherry_3494']],

    ['cmd K', 'up '   * 6          , ['Skim']],
    ['cmd J', 'down ' * 6          , ['Skim']],
    ['alt L', 'ctrl_r tab'         , ['Skim']],
    ['alt H', 'ctrl_r shift_r tab' , ['Skim']],

    ['cmd K', 'up '   * 30         , ['Google Chrome']],
    ['cmd J', 'down ' * 30         , ['Google Chrome']],
    ['alt L', 'ctrl_r tab'         , ['Google Chrome']],
    ['alt H', 'ctrl_r shift_r tab' , ['Google Chrome']],
    ['ctrl l', 'cmd_r l'           , ['Google Chrome']],

    ['ctrl P'      , 'up '   * 6 , ['Skim']],
    ['ctrl N'      , 'down ' * 6 , ['Skim']],
    ['alt shift ,' , 'fn left'   , ['Skim']],
    ['alt shift .' , 'fn right'  , ['Skim']],

    ['ctrl D' , 'cmd_r del'   , ['Xee³']],
    ['ctrl P' , 'cmd_r left'  , ['Xee³']],
    ['ctrl N' , 'cmd_r right' , ['Xee³']],

    ['alt shift ,' , 'alt_r up'   , ['Finder']],
    ['alt shift .' , 'alt_r down' , ['Finder']],

    ['alt shift ,' , 'cmd_r up'   , ['Sublime Text']],
    ['alt shift .' , 'cmd_r down' , ['Sublime Text']],
    ['ctrl P'      , 'up'         , ['Sublime Text']],
    ['ctrl N'      , 'down'       , ['Sublime Text']],

    ['ctrl P' , 'up'   , ['!emacs_ignore_app', '!Skim', '!Xee³']],
    ['ctrl N' , 'down' , ['!emacs_ignore_app', '!Skim', '!Xee³']],
    ['ctrl D' , 'fdel' , ['!emacs_ignore_app', '!Skim', '!Xee³']],

    ['alt shift ,' , 'cmd_r up'   , ['!emacs_ignore_app', '!Skim', '!Finder', '!Sublime Text']],
    ['alt shift .' , 'cmd_r down' , ['!emacs_ignore_app', '!Skim', '!Finder', '!Sublime Text']],

    ['ctrl B' , 'left'        , ['!emacs_ignore_app']],
    ['ctrl F' , 'right'       , ['!emacs_ignore_app']],
    ['alt B'  , 'alt_r left'  , ['!emacs_ignore_app']],
    ['alt F'  , 'alt_r right' , ['!emacs_ignore_app']],
    ['ctrl A' , 'cmd_r left'  , ['!emacs_ignore_app']],
    ['ctrl E' , 'cmd_r right' , ['!emacs_ignore_app']],
    ['ctrl H' , 'del'         , ['!emacs_ignore_app']],
    ['alt D'  , 'alt_r fdel'  , ['!emacs_ignore_app']],
    ['ctrl U' , 'cmd_r right cmd_r shift_r left del del norepeat', ['!emacs_ignore_app']],

    ['ctrl cmd F' , 'cmd_r return'                   , ['TERMINAL']],
    ['ctrl cmd F' , 'cmd_r shift_r F cmd_r shift_r -', ['Skim', 'Kindle']],
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

    ['ctrl tab'      , 'cmd_r alt_r right', ['Bilibili']],
    ['ctrl shift tab', 'cmd_r alt_r left' , ['Bilibili']],

    ['left' , 'cmd_r left' , ['Xee³']],
    ['up'   , 'cmd_r left' , ['Xee³']],
    ['H'    , 'cmd_r left' , ['Xee³']],
    ['K'    , 'cmd_r left' , ['Xee³']],
    ['right', 'cmd_r right', ['Xee³']],
    ['down' , 'cmd_r right', ['Xee³']],
    ['J'    , 'cmd_r right', ['Xee³']],
    ['L'    , 'cmd_r right', ['Xee³']],

    ['cmd P', 'cmd_r alt_r G', ['Skim']],
]
