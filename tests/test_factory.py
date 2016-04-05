# -*- coding: utf-8 -*-
from easy_karabiner.factory import *


def test_create_keymap():
    raw_keymap = [
        'KeyToKey',
        ['ctrl'],
        ['f12'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __KeyToKey__
            KeyCode::CONTROL_L,
            KeyCode::F12
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'KeyToKey',
        ['ctrl', 'U'],
        ['end', 'shift_r', 'home', 'del', 'del', 'norepeat'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __KeyToKey__
            KeyCode::U, ModifierFlag::CONTROL_L, ModifierFlag::NONE,
            KeyCode::END, KeyCode::HOME, ModifierFlag::SHIFT_R,
            KeyCode::DELETE, KeyCode::DELETE, Option::NOREPEAT
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'KeyToKey',
        ['alt', 'shift', ','],
        ['fn', 'left'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __KeyToKey__
            KeyCode::COMMA, ModifierFlag::OPTION_L, ModifierFlag::SHIFT_L, ModifierFlag::NONE,
            KeyCode::CURSOR_LEFT, ModifierFlag::FN
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'DropAllKeys',
        ['ModifierFlag::MY_VI_MODE'],
        ['DROPALLKEYS_DROP_KEY', 'DROPALLKEYS_DROP_CONSUMERKEY', 'DROPALLKEYS_DROP_POINTINGBUTTON'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __DropAllKeys__
            ModifierFlag::MY_VI_MODE,
            Option::DROPALLKEYS_DROP_KEY,
            Option::DROPALLKEYS_DROP_CONSUMERKEY,
            Option::DROPALLKEYS_DROP_POINTINGBUTTON
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'SimultaneousKeyPresses',
        ['9', '0', '9', 'shift'],
        ['shift', '0', 'left']
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __SimultaneousKeyPresses__
          @begin
          KeyCode::KEY_9, KeyCode::KEY_0, KeyCode::KEY_9, ModifierFlag::SHIFT_L
          @end

          @begin
          KeyCode::KEY_0, ModifierFlag::SHIFT_L, KeyCode::CURSOR_LEFT
          @end
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'DoublePressModifier',
        ['fn'],
        ['cmd', 'alt', 'I'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __DoublePressModifier__
          KeyCode::FN,
          @begin
          KeyCode::FN
          @end
          @begin
          KeyCode::I, ModifierFlag::COMMAND_L, ModifierFlag::OPTION_L
          @end
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'DoublePressModifier',
        ['fn'],
        ['F12'],
        ['F11'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __DoublePressModifier__
          KeyCode::FN,
          @begin
          KeyCode::F11
          @end
          @begin
          KeyCode::F12
          @end
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'HoldingKeyToKey',
        ['esc'],
        ['cmd_r', 'ctrl_r', 'alt_r', 'shift_r'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __HoldingKeyToKey__
          KeyCode::ESCAPE,
          @begin
          KeyCode::ESCAPE
          @end
          @begin
          KeyCode::COMMAND_R, ModifierFlag::CONTROL_R, ModifierFlag::OPTION_R, ModifierFlag::SHIFT_R
          @end
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'KeyOverlaidModifier',
        ['caps'],
        ['esc'],
        ['ctrl'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __KeyOverlaidModifier__
          KeyCode::CAPSLOCK,
          @begin
          KeyCode::CONTROL_L
          @end
          @begin
          KeyCode::ESCAPE
          @end
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'KeyDownUpToKey',
        ['cmd', ','],
        ['cmd', 'shift', 'left'],
        ['cmd', 'left'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __KeyDownUpToKey__
          KeyCode::COMMA, ModifierFlag::COMMAND_L, ModifierFlag::NONE,
          @begin
          KeyCode::CURSOR_LEFT, ModifierFlag::COMMAND_L, ModifierFlag::SHIFT_L
          @end
          @begin
          KeyCode::CURSOR_LEFT, ModifierFlag::COMMAND_L
          @end
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'BlockUntilKeyUp',
        ['sp']
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __BlockUntilKeyUp__
          KeyCode::SPACE
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'DropKeyAfterRemap',
        ['mission_control', 'MODIFIERFLAG_EITHER_LEFT_OR_RIGHT_SHIFT']
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __DropKeyAfterRemap__
          KeyCode::MISSION_CONTROL,
          MODIFIERFLAG_EITHER_LEFT_OR_RIGHT_SHIFT
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'PassThrough',
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '<autogen> __PassThrough__ </autogen>'
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'double',
        ['cmd', 'K'],
        ['up'] * 6,
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __DoublePressModifier__
          KeyCode::K, ModifierFlag::COMMAND_L, ModifierFlag::NONE,

          @begin
          KeyCode::K, ModifierFlag::COMMAND_L
          @end

          @begin
          KeyCode::CURSOR_UP, KeyCode::CURSOR_UP, KeyCode::CURSOR_UP,
          KeyCode::CURSOR_UP, KeyCode::CURSOR_UP, KeyCode::CURSOR_UP
          @end
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'DoublePressModifier',
        ['cmd', 'J'],
        ['down'] * 6,
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __DoublePressModifier__
          KeyCode::J, ModifierFlag::COMMAND_L, ModifierFlag::NONE,

          @begin
          KeyCode::J, ModifierFlag::COMMAND_L
          @end

          @begin
          KeyCode::CURSOR_DOWN, KeyCode::CURSOR_DOWN, KeyCode::CURSOR_DOWN,
          KeyCode::CURSOR_DOWN, KeyCode::CURSOR_DOWN, KeyCode::CURSOR_DOWN
          @end
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'KeyToKey',
        ['alt', 'E'],
        ['KeyCode::VK_OPEN_URL_FINDER'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __KeyToKey__
            KeyCode::E, ModifierFlag::OPTION_L, ModifierFlag::NONE,
            KeyCode::VK_OPEN_URL_FINDER
        </autogen>'''
    util.assert_xml_equal(k, s)

    raw_keymap = [
        'FlipScrollWheel',
        ['FLIPSCROLLWHEEL_HORIZONTAL', 'FLIPSCROLLWHEEL_VERTICAL'],
    ]
    k = KeymapCreater.create(raw_keymap)
    s = '''
        <autogen> __FlipScrollWheel__
          Option::FLIPSCROLLWHEEL_HORIZONTAL,
          Option::FLIPSCROLLWHEEL_VERTICAL
        </autogen>'''
    util.assert_xml_equal(k, s)


def test_create_definition():
    d = DefinitionCreater.create('KINDLE', ['com.amazon.Kindle'])
    s = '''
        <appdef>
          <appname>KINDLE</appname>
          <equal>com.amazon.Kindle</equal>
        </appdef>'''
    util.assert_xml_equal(d[0], s)

    d = DefinitionCreater.create('EMACS_IGNORE_APP', [
            'ECLIPSE', 'EMACS', 'TERMINAL',
            'REMOTEDESKTOPCONNECTION', 'VI', 'X11',
            'VIRTUALMACHINE', 'TERMINAL', 'SUBLIMETEXT',
        ])
    s = '''
        <replacementdef>
          <replacementname>EMACS_IGNORE_APP</replacementname>
          <replacementvalue>
            ECLIPSE, EMACS, TERMINAL,
            REMOTEDESKTOPCONNECTION, VI, X11,
            VIRTUALMACHINE, TERMINAL, SUBLIMETEXT
          </replacementvalue>
        </replacementdef>'''
    util.assert_xml_equal(d[0], s)

    d1, d2 = DefinitionCreater.create('CHERRY_3494', ['0x046a', '0x0011'])
    s1 = '''
        <devicevendordef>
          <vendorname>CHERRY_3494_VENDOR</vendorname>
          <vendorid>0x046a</vendorid>
        </devicevendordef>
        '''
    s2 = '''
        <deviceproductdef>
          <productname>CHERRY_3494_PRODUCT</productname>
          <productid>0x0011</productid>
        </deviceproductdef>
        '''
    util.assert_xml_equal(d1, s1)
    util.assert_xml_equal(d2, s2)

    d = DefinitionCreater.create('Open::FINDER', ['/Applications/Finder.app'])
    s = '''
        <vkopenurldef>
          <name>KeyCode::VK_OPEN_URL_FINDER</name>
          <url type="file">/Applications/Finder.app</url>
        </vkopenurldef>'''
    util.assert_xml_equal(d[0], s)


def test_create_filter():
    f = FilterCreater.create('LOGITECH')
    s = '''<device_only> DeviceVendor::LOGITECH </device_only>'''
    util.assert_xml_equal(f[0], s)

    f = FilterCreater.create('!EMACS_MODE_IGNORE_APPS')
    s = '''<not> {{EMACS_MODE_IGNORE_APPS}} </not>'''
    util.assert_xml_equal(f[0], s)


def test_create_keymaps():
    raw_keymaps = [
        ['KeyToKey', ['Cmd'], ['Alt']],
        ['double', ['fn'], ['f12']],
        ['holding', ['ctrl'], ['cmd', 'alt', 'ctrl'], ['esc']],
    ]
    outputs = [
        '''
        <autogen> __KeyToKey__
          KeyCode::COMMAND_L,
          KeyCode::OPTION_L
        </autogen>
        ''',
        '''
        <autogen> __DoublePressModifier__
          KeyCode::FN,
          @begin KeyCode::FN @end
          @begin KeyCode::F12 @end
        </autogen>
        ''',
        '''
        <autogen> __HoldingKeyToKey__
          KeyCode::CONTROL_L,
          @begin KeyCode::ESCAPE @end
          @begin KeyCode::COMMAND_L, ModifierFlag::OPTION_L, ModifierFlag::CONTROL_L @end
        </autogen>
        ''',
    ]
    keymap_objs = create_keymaps(raw_keymaps)
    assert(len(keymap_objs) == len(outputs))
    for i in range(len(outputs)):
        util.assert_xml_equal(keymap_objs[i], outputs[i])


def test_create_definitions():
    definitions = {
        'BILIBILI': 'com.typcn.Bilibili',
        'CHERRY_3494': ['0x046a', '0x0011'],
        'UIElementRole::custom_ui': 'used as a filter',
        'replacement_example': ['for', 'example', 'Xee'],
    }
    outputs = [
        '''
        <appdef>
          <appname>BILIBILI</appname>
          <equal>com.typcn.Bilibili</equal>
        </appdef>
        ''',
        '''
        <devicevendordef>
          <vendorname>CHERRY_3494_VENDOR</vendorname>
          <vendorid>0x046a</vendorid>
        </devicevendordef>
        ''',
        '''
        <deviceproductdef>
          <productname>CHERRY_3494_PRODUCT</productname>
          <productid>0x0011</productid>
        </deviceproductdef>
        ''',
        '''
        <uielementroledef>custom_ui</uielementroledef>
        ''',
        '''
        <replacementdef>
          <replacementname>replacement_example</replacementname>
          <replacementvalue>for, example, Xee</replacementvalue>
        </replacementdef>
        ''',
    ]
    definition_objs = create_definitions(definitions)
    assert(len(definition_objs) == len(outputs))
    for i in range(len(outputs)):
        util.assert_xml_equal(definition_objs[i], outputs[i])


def test_create_filters():
    f = create_filters(['LOGITECH', 'LOGITECH_USB_RECEIVER'])
    s = '''
        <device_only>
          DeviceVendor::LOGITECH,
          DeviceProduct::LOGITECH_USB_RECEIVER
        </device_only>'''
    util.assert_xml_equal(f[0], s)

    f = create_filters(['!EMACS_MODE_IGNORE_APPS', '!FINDER', '!SKIM'])
    s = '''
        <not>
          {{EMACS_MODE_IGNORE_APPS}}, FINDER, SKIM
        </not>'''
    util.assert_xml_equal(f[0], s)
