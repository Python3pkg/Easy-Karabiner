# -*- coding: utf-8 -*-
from easy_karabiner.query import *


def test_alias():
    aliases_table = {
        'MODIFIER_ALIAS': {
            'command': 'COMMAND_R',
        },
        'KEY_ALIAS': {
            'scroll_flip': 'FLIPSCROLLWHEEL_VERTICAL',
            'none': 'ModifierFlag::None',
        }
    }
    update_aliases(aliases_table)
    assert(get_def_alias('open') == 'VKOpenURL')
    assert(get_key_alias('command') == 'COMMAND_R')
    assert(get_keymap_alias('press_modifier') == 'KeyOverlaidModifier')

    assert(query_filter_class_names('EMACS') == ['Filter'])
    assert(query_filter_class_names('ModifierFlag::COMMAND_R') == ['ModifierFilter'])
    assert(query_filter_class_names('ctrl') == ['ModifierFilter'])
    assert(query_filter_class_names('COMMAND_R') == ['ModifierFilter'])

    assert(KeyHeaderQuery.query('FN') == 'ModifierFlag')
    assert(DefinitionTypeQuery.query('EMACS') == 'appdef')
    assert(DefinitionTypeQuery.query('FN') == 'modifierdef')
