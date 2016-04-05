# -*- coding: utf-8 -*-
import os


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), 'data')


def get_data_path(filename):
    return os.path.join(get_data_dir(), filename)


def get_karabiner_app_path():
    return '/Applications/Karabiner.app'


def _get_path_relate_to_karabiner(relative_path):
    return os.path.join(get_karabiner_app_path(), relative_path)


def get_karabiner_bin_dir():
    return _get_path_relate_to_karabiner('Contents/Library/bin')


def get_karabiner_resources_dir():
    return _get_path_relate_to_karabiner('Contents/Resources')


def get_karabiner_bin(filename):
    return os.path.join(get_karabiner_bin_dir(), filename)
