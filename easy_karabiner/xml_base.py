# -*- coding: utf-8 -*-
import lxml.etree as etree
import xml.dom.minidom as minidom


class XML_base(object):
    @staticmethod
    def create_tag(name, text='', **kwargs):
        et = ElementTree.Element(name, **kwargs)
        et.text = text
        return et

    @staticmethod
    def to_format_str(xml_tree):
        formatter = xmlformatter.Formatter()
        rough_string = ElementTree.tostring(xml_tree, 'UTF-8')
        rough_string = unescape(rough_string)
        return formatter.format_string(rough_string)

    @staticmethod
    def parse(filepath):
        return etree.parse(filepath).getroot()

    @staticmethod
    def parse_string(xmlstr):
        return etree.fromstring(xmlstr)

    def to_xml(self):
        raise Exception('Need override')

    def to_str(self):
        return self.to_format_str(self.to_xml())

    def __str__(self):
        lines = self.to_str().split('\n')
        return '\n'.join(lines[1:])