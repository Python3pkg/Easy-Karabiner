# -*- coding: utf-8 -*-
import inspect
from .xml_base import XML_base


class Hashable(object):
    def _id(self):
        raise Exception('Need override')

    def __hash__(self):
        return hash(self._id())

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._id() == other._id()


def find_all_subclass_of(superclass, global_vars):
    # remove start with '_'
    names = filter(lambda name: not name.startswith('_'), global_vars.keys())
    # remove name which is not a class name
    names = filter(lambda name: inspect.isclass(global_vars[name]), names)
    # remove class name which is not a subclass of superclass
    names = filter(lambda name: issubclass(global_vars[name], superclass), names)
    return map(global_vars.get, names)


# TODO: compare string with parse as xml tree, and strip spaces when compare text
def compare_xml_with_xml(xml_tree1, xml_tree2):
    pass

def compare_xml_with_str(xml_tree, xml_str):
    # XML_base.
    pass