# -*- coding: utf-8 -*-
from easy_karabiner.query import DefinitionBucket
from easy_karabiner.parse import *


def test_alias():
    definitions = {
        'BILIBILI': 'com.typcn.Bilibili',
        'CHERRY_3494': ['0x046a', '0x0011'],
        'UIElementRole::custom_ui': 'used as filter',
        'error': 'because value not valid',
        'replacement_test': ['for', 'example', 'Xee'],
    }

    maps = [
        ['cmd', 'alt'],
        ['_double_', 'shift', '#! osascript -e \'display notification "test1"\''],
        ['alt mouse_left', 'mouse_left "#! osascript -e \'display notification \\"test2\\"\'"'],
        ['alt E', 'Finder', ['UIElementRole::custom_ui']],
        ['__FlipScrollWheel__', 'flipscrollwheel_vertical', ['Finder', 'cmd', 'built_in_keyboard_and_trackpad']],
        ['ctrl cmd F', 'cmd F', ['VIRTUALMACHINE']],
    ]

    result = '''
    <appdef>
      <appname>BILIBILI</appname>
      <equal>com.typcn.Bilibili</equal>
    </appdef>
    <appdef>
      <appname>Finder</appname>
      <equal>com.apple.finder</equal>
    </appdef>
    <deviceproductdef>
      <productname>CHERRY_3494_PRODUCT</productname>
      <productid>0x0011</productid>
    </deviceproductdef>
    <deviceproductdef>
      <productname>built_in_keyboard_and_trackpad_PRODUCT</productname>
      <productid>0x0259</productid>
    </deviceproductdef>
    <devicevendordef>
      <vendorname>CHERRY_3494_VENDOR</vendorname>
      <vendorid>0x046a</vendorid>
    </devicevendordef>
    <devicevendordef>
      <vendorname>built_in_keyboard_and_trackpad_VENDOR</vendorname>
      <vendorid>0x05ac</vendorid>
    </devicevendordef>
    <replacementdef>
      <replacementname>replacement_test</replacementname>
      <replacementvalue>for, example, Xee</replacementvalue>
    </replacementdef>
    <uielementroledef>custom_ui</uielementroledef>
    <vkopenurldef>
      <name>KeyCode::VK_OPEN_URL_760efb2</name>
      <url type="shell">
    <![CDATA[osascript -e 'display notification "test2"']]>  </url>
    </vkopenurldef>
    <vkopenurldef>
      <name>KeyCode::VK_OPEN_URL_Finder</name>
      <url type="file">/System/Library/CoreServices/Finder.app</url>
    </vkopenurldef>
    <vkopenurldef>
      <name>KeyCode::VK_OPEN_URL_aedd86e</name>
      <url type="shell">
    <![CDATA[osascript -e 'display notification "test1"']]>  </url>
    </vkopenurldef>
    <block>
      <autogen> __KeyToKey__
        KeyCode::COMMAND_L,
        KeyCode::OPTION_L
      </autogen>
      <autogen> __DoublePressModifier__
        KeyCode::SHIFT_L,
        @begin
        KeyCode::SHIFT_L
        @end
        @begin
        KeyCode::VK_OPEN_URL_aedd86e
        @end
      </autogen>
      <autogen> __KeyToKey__
        PointingButton::LEFT, ModifierFlag::OPTION_L, ModifierFlag::NONE,
        PointingButton::LEFT, KeyCode::VK_OPEN_URL_760efb2
      </autogen>
    </block>
    <block>
      <uielementrole_only>custom_ui</uielementrole_only>
      <autogen> __KeyToKey__
        KeyCode::E, ModifierFlag::OPTION_L, ModifierFlag::NONE,
        KeyCode::VK_OPEN_URL_Finder
      </autogen>
    </block>
    <block>
      <device_only>
        DeviceVendor::built_in_keyboard_and_trackpad_VENDOR,
        DeviceProduct::built_in_keyboard_and_trackpad_PRODUCT
      </device_only>
      <modifier_only>ModifierFlag::COMMAND_L</modifier_only>
      <only>Finder</only>
      <autogen> __FlipScrollWheel__
        Option::FLIPSCROLLWHEEL_VERTICAL
      </autogen>
    </block>
    <block>
      <only>VIRTUALMACHINE</only>
      <autogen> __KeyToKey__
        KeyCode::F, ModifierFlag::CONTROL_L, ModifierFlag::COMMAND_L, ModifierFlag::NONE,
        KeyCode::F, ModifierFlag::COMMAND_L
      </autogen>
    </block>
    '''

    DefinitionBucket.clear()
    block_objs, definition_objs = parse(maps=maps, definitions=definitions)
    s = ''.join(obj.to_str(remove_first_line=True) for obj in (definition_objs + block_objs))
    s = ''.join(s.split())
    result = ''.join(result.split())
    assert(s == result)
