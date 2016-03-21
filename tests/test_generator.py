# -*- coding: utf-8 -*-
from easy_karabiner import util
from easy_karabiner import __version__
from easy_karabiner.generator import *


def test_generator():
    DEFINITIONS = {
        'DeviceVendor::CHERRY': '0x046a',
        'DeviceProduct::3494' : '0x0011',
    }
    REMAPS = [
        ['alt', 'cmd', ('CHERRY', '3494')],
        ['cmd', 'alt', ('CHERRY', '3494')],
    ]
    g = Generator(remaps=REMAPS, definitions=DEFINITIONS)
    s = '''
        <root>
          <Easy-Karabiner>{version}</Easy-Karabiner>
          <item>
            <name>Easy-Karabiner</name>
            <deviceproductdef>
              <productname>3494</productname>
              <productid>0x0011</productid>
            </deviceproductdef>
            <devicevendordef>
              <vendorname>CHERRY</vendorname>
              <vendorid>0x046a</vendorid>
            </devicevendordef>
            <item>
              <name>Enable</name>
              <identifier>private.easy_karabiner</identifier>
              <block>
                <device_only> DeviceVendor::CHERRY, DeviceProduct::3494 </device_only>
                <autogen> __KeyToKey__ KeyCode::OPTION_L, KeyCode::COMMAND_L </autogen>
                <autogen> __KeyToKey__ KeyCode::COMMAND_L, KeyCode::OPTION_L </autogen>
              </block>
            </item>
          </item>
        </root>
        '''.format(version=__version__)
    util.assert_xml_equal(g, s)