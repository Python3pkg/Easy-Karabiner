DEFINITIONS = {
    'error': 'because value not valid',
    # app
    'BILIBILI': 'com.typcn.Bilibili',
    # replacement
    '可以是中文': ('比如', 'hello', 'Xee³'),
    # device
    'CHERRY_3494': ['0x046a', '0x0011'],
    'UIElementRole::自定义UI组件': '用作 filter',
    # modifierdef
    'Modifier::KEYLOCK': '',
}

MAPS = [
    ['cmd', 'alt'],
    ['_double_', 'shift', '#! osascript -e \'display notification "test1"\''],
    ['alt mouse_left', 'mouse_left "#! osascript -e \'display notification \\"test2\\"\'"'],
    ['alt E', 'Finder', ['UIElementRole::自定义UI组件']],
    ['alt X', 'Xee³.app', ['Finder', 'cmd']],
    ['__FlipScrollWheel__', 'flipscrollwheel_vertical', ['Xee³.app', 'built_in_keyboard_and_trackpad']],
    ['ctrl cmd F', 'cmd F', ['VIRTUALMACHINE']],
    ['alt', 'none', ['KEYLOCK']],
    ['cmd', 'none', ['Modifier::KEYLOCK']],
]
