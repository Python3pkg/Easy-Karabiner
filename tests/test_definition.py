# -*- coding: utf-8 -*-
from easy_karabiner import util
from easy_karabiner.definition import *


def test_appdef():
    d = App('BILIBILI', 'com.typcn.Bilibili')
    s = '''
        <appdef>
          <appname>BILIBILI</appname>
          <equal>com.typcn.Bilibili</equal>
        </appdef>'''
    util.assert_xml_equal(d, s)

    d = App('PQRS', 'org.pqrs.aaa', 'org.pqrs.ccc.', '.local')
    s = '''
        <appdef>
          <appname>PQRS</appname>
          <equal>org.pqrs.aaa</equal>
          <prefix>org.pqrs.ccc.</prefix>
          <suffix>.local</suffix>
        </appdef>'''
    util.assert_xml_equal(d, s)


def test_windownamedef():
    d = WindowName('Google_Search', ' - Google Search$', 'Search$')
    s = '''
        <windownamedef>
          <name>Google_Search</name>
          <regex> - Google Search$</regex>
          <regex>Search$</regex>
        </windownamedef>'''
    util.assert_xml_equal(d, s)


def test_devicedef():
    d = DeviceVendor('HEWLETT_PACKARD', '0x03f0')
    s = '''
        <devicevendordef>
          <vendorname>HEWLETT_PACKARD</vendorname>
          <vendorid>0x03f0</vendorid>
        </devicevendordef>'''
    util.assert_xml_equal(d, s)

    d = DeviceProduct('MY_HP_KEYBOARD', '0x0224')
    s = '''
        <deviceproductdef>
          <productname>MY_HP_KEYBOARD</productname>
          <productid>0x0224</productid>
        </deviceproductdef>'''
    util.assert_xml_equal(d, s)


def test_inputsourcedef():
    d = InputSource('AZERTY',
                    'com.apple.keylayout.ABC-AZERTY',
                    'com.apple.keylayout.French')
    s = '''
        <inputsourcedef>
          <name>AZERTY</name>
          <inputsourceid_equal>com.apple.keylayout.ABC-AZERTY</inputsourceid_equal>
          <inputsourceid_equal>com.apple.keylayout.French</inputsourceid_equal>
        </inputsourcedef>'''
    util.assert_xml_equal(d, s)

    d = InputSource('CHINESE', 'zh-Hans', 'zh-Hant')
    s = '''
        <inputsourcedef>
          <name>CHINESE</name>
          <languagecode>zh-Hans</languagecode>
          <languagecode>zh-Hant</languagecode>
        </inputsourcedef>'''
    util.assert_xml_equal(d, s)

    d = InputSource('DVORAK',
                    'com.apple.keylayout.Dvorak.',
                    'com.apple.keylayout.DVORAK.')
    s = '''
        <inputsourcedef>
          <name>DVORAK</name>
          <inputsourceid_prefix>com.apple.keylayout.Dvorak</inputsourceid_prefix>
          <inputsourceid_prefix>com.apple.keylayout.DVORAK</inputsourceid_prefix>
        </inputsourcedef>'''
    util.assert_xml_equal(d, s)

    d = VKChangeInputSource('TEST_ALL', 'com.example.equal', 'com.example.prefix.', 'en-US')
    s = '''
        <vkchangeinputsourcedef>
          <name>TEST_ALL</name>
          <inputsourceid_equal>com.example.equal</inputsourceid_equal>
          <inputsourceid_prefix>com.example.prefix</inputsourceid_prefix>
          <languagecode>en-US</languagecode>
        </vkchangeinputsourcedef>'''
    util.assert_xml_equal(d, s)


def test_vkopenurldef():
    d = VKOpenURL('KeyCode::VK_OPEN_URL_karabiner', 'https://pqrs.org/osx/karabiner/')
    s = '''
        <vkopenurldef>
          <name>KeyCode::VK_OPEN_URL_karabiner</name>
          <url>https://pqrs.org/osx/karabiner/</url>
        </vkopenurldef>'''
    util.assert_xml_equal(d, s)

    d = VKOpenURL('KeyCode::VK_OPEN_URL_FINDER', '/Applications/Finder.app', background=True)
    s = '''
        <vkopenurldef>
          <name>KeyCode::VK_OPEN_URL_FINDER</name>
          <url type="file">/Applications/Finder.app</url>
          <background/>
        </vkopenurldef>'''
    util.assert_xml_equal(d, s)

    d = VKOpenURL('KeyCode::VK_OPEN_URL_Calculator', '/Applications/Calculator.app')
    s = '''
        <vkopenurldef>
          <name>KeyCode::VK_OPEN_URL_Calculator</name>
          <url type="file">/Applications/Calculator.app</url>
        </vkopenurldef>'''
    util.assert_xml_equal(d, s)

    d = VKOpenURL('KeyCode::VK_OPEN_URL_date_pbcopy', '#! /bin/date | /usr/bin/pbcopy')
    s = '''
        <vkopenurldef>
          <name>KeyCode::VK_OPEN_URL_date_pbcopy</name>
          <url type="shell"><![CDATA[/bin/date | /usr/bin/pbcopy]]></url>
        </vkopenurldef>'''
    util.assert_xml_equal(d, s)


def test_replacementdef():
    d = Replacement('EMACS_IGNORE_APP',
                    'ECLIPSE', 'EMACS', 'TERMINAL',
                    'REMOTEDESKTOPCONNECTION', 'VI', 'X11',
                    'VIRTUALMACHINE', 'TERMINAL', 'SUBLIMETEXT')
    s = '''
        <replacementdef>
          <replacementname>EMACS_IGNORE_APP</replacementname>
          <replacementvalue>
            ECLIPSE, EMACS, TERMINAL,
            REMOTEDESKTOPCONNECTION, VI, X11,
            VIRTUALMACHINE, TERMINAL, SUBLIMETEXT
          </replacementvalue>
        </replacementdef>'''
    util.assert_xml_equal(d, s)


def test_uielementrole():
    d = UIElementRole('AXTextField')
    s = '''<uielementroledef> AXTextField </uielementroledef>'''
    util.assert_xml_equal(d, s)
