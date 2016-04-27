from typing import TypeVar, Dict, Tuple, List
from .definition import DefinitionBase
from .filter import FilterBase
from .keymap import KeyToKeyBase

Iter = TypeVar('Iter', List, Tuple)
RawEntry = TypeVar('RawEntry', str, Iter)
RawDefinitions = Dict[str:RawEntry]
RawMap = Iter[RawEntry]
RawMaps = Iter[RawMap]
RawKeymap = TypeVar('RawKeymap',
                    Iter[str],
                    Iter[str, Iter[str]],
                    Iter[str, Iter[str], Iter[str]],
                    Iter[str, Iter[str], Iter[str], Iter[str]])
RawFilters = TypeVar('RawFilters', Tuple[str])


def define_filters(raw_filters: RawFilters) -> None: ...
def define_keymaps(raw_keymaps: Iter[RawKeymap]) -> None: ...
def create_filters(raw_filters: RawFilters) -> Iter[FilterBase]: ...
def create_definitions(definitions: RawDefinitions) -> Iter[DefinitionBase]: ...


class FilterCreater(object):
    @classmethod
    def define(cls, val: str) -> None: ...

    @classmethod
    def create(cls, raw_val: str) -> Iter[FilterBase]: ...

    @classmethod
    def escape_filter_name(cls, class_name: str, name_val: str) -> str: ...


class KeymapCreater(object):
    @classmethod
    def define_key(cls, val: str) -> None: ...

    @classmethod
    def create(cls, raw_keymap: RawKeymap) -> KeyToKeyBase: ...

    @classmethod
    def get_karabiner_format_key(cls, key: str) -> str: ...


class DefinitionCreater(object):
    @classmethod
    def create(cls, raw_name: str, vals: Iter[str]) -> Iter[DefinitionBase]: ...

    @classmethod
    def define(cls, class_name: str,
                    raw_name: str,
                    def_name: str,
                    vals: Iter[str],
                    escape_def_name: bool) -> Iter[DefinitionBase]: ...

    @classmethod
    def define_replacement(cls, raw_name: str, vals: Iter[str]) -> Iter[DefinitionBase]: ...

    @classmethod
    def define_device(cls, raw_name: str, vals: Iter[str]) -> Iter[DefinitionBase]: ...

    @classmethod
    def define_app(cls, raw_name: str, bundle_id: str) -> Iter[DefinitionBase]: ...

    @classmethod
    def define_open(cls, val: str, index: str) -> Iter[DefinitionBase]: ...

    @classmethod
    def escape_def_name(cls, def_name: str, class_name: str) -> str: ...


class DefinitionDetector(object):
    @classmethod
    def is_device(cls, vals: Iter[str]) -> bool: ...

    @classmethod
    def is_vkopenurl(cls, val: str) -> bool: ...

    @classmethod
    def is_uielementrole(cls, val: str) -> bool: ...

    @classmethod
    def is_app(cls, val: str) -> bool: ...

    @classmethod
    def is_all_app(cls, vals: Iter[str]) -> bool: ...

    @classmethod
    def is_replacement(cls, val: str) -> bool: ...

    @classmethod
    def is_keymap(cls, val: str) -> bool: ...

    @classmethod
    def get_definition_caregory(cls, def_class: DefinitionBase) -> str: ...
