# -*- coding: utf-8 -*-
from __future__ import print_function
import lxml.etree as etree
import xml.dom.minidom as minidom
from . import exception
from .fucking_string import ensure_utf8


class BaseXML(object):
    @classmethod
    def parse(cls, filepath):
        return etree.parse(filepath).getroot()

    @classmethod
    def parse_string(cls, xml_str):
        return etree.fromstring(xml_str)

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @classmethod
    def create_cdata_text(cls, text):
        return etree.CDATA(text)

    @classmethod
    def assign_text_attribute(cls, etree_element, text):
        if text is not None and not isinstance(text, etree.CDATA):
            etree_element.text = ensure_utf8(text)
        else:
            etree_element.text = text

    @classmethod
    def create_tag(cls, name, text=None, **kwargs):
        et = etree.Element(name, **kwargs)
        cls.assign_text_attribute(et, text)
        return et

    @classmethod
    def pretty_text(cls, elem, indent="  ", level=0):
        ''' NOTICE: This method would change the construct of XML tree '''
        i = "\n" + level * indent

        if len(elem) == 0:
            if elem.text is not None:
                lines = elem.text.split('\n')
                if len(lines) > 1:
                    if not lines[0].startswith(' '):
                        lines[0] = (i + indent) + lines[0]
                    if lines[-1].strip() == '':
                        lines.pop()
                    elem.text = (i + indent).join(lines) + i
        else:
            for subelem in elem:
                BaseXML.pretty_text(subelem, indent, level + 1)

        return elem

    @classmethod
    def to_format_str(cls, xml_tree, pretty_text=True):
        indent = "  "
        if pretty_text:
            BaseXML.pretty_text(xml_tree, indent=indent)
        xml_string = etree.tostring(xml_tree)
        xml_string = minidom.parseString(xml_string).toprettyxml(indent=indent)
        return xml_string

    def to_xml(self):
        '''NOTICE: This method must be a REENTRANT function, which means
        it should NOT change status or modify any member of `self` object.
        Because other methods may change the construct of the XML tree.
        '''
        raise exception.NeedOverrideError()

    def to_str(self, pretty_text=True, remove_first_line=False):
        xml_str = self.to_format_str(self.to_xml(), pretty_text=pretty_text)

        if remove_first_line:
            lines = xml_str.split('\n')
            if len(lines[-1].strip()) == 0:
                # remove last blank line
                lines = lines[1:-1]
            else:
                lines = lines[1:]
            return '\n'.join(lines)
        else:
            return xml_str

    def __str__(self):
        # remove version tag
        return self.to_str(remove_first_line=True)
