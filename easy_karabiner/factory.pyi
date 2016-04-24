from typing import TypeVar, Dict, Tuple, List, Iterable as Iter
from .definition import DefinitionBase
from .filter import FilterBase
from .keymap import KeyToKeyBase

RawEntry = TypeVar('RawEntry', str, List)
RawDefinitions = Dict[str:RawEntry]
RawMap = List[RawEntry]
RawMaps = List[RawMap]
RawKeymap = TypeVar('RawKeymap',
                    Tuple[str],
                    Tuple[str, Tuple[str]],
                    Tuple[str, Tuple[str], Tuple[str]],
                    Tuple[str, Tuple[str], Tuple[str], Tuple[str]])
RawFilters = TypeVar('RawFilters', Tuple[str])


def define_filters(raw_filters: RawFilters) -> None: ...
def define_keymaps(raw_keymaps: Iter[RawKeymap]) -> None: ...
def create_filters(raw_filters: RawFilters) -> List[FilterBase]: ...
def create_definitions(definitions: RawDefinitions) -> List[DefinitionBase]: ...


class FilterCreater(object):
    @classmethod
    def define(cls, val: str) -> None: ...

    @classmethod
    def create(cls, raw_val: str) -> List[FilterBase]: ...

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
    def create(cls, raw_name: str, vals: List[str]) -> Iter[DefinitionBase]: ...

    @classmethod
    def define(cls, class_name: str,
                    raw_name: str,
                    def_name: str,
                    vals: Iter[str],
                    escape_def_name: bool) -> List[DefinitionBase]: ...

    @classmethod
    def define_device(cls, raw_name: str, vals: Iter[str]) -> List[DefinitionBase]: ...

    @classmethod
    def define_app(cls, raw_name: str, bundle_id: str) -> List[DefinitionBase]: ...

    @classmethod
    def define_open(cls, val: str, index: str) -> List[DefinitionBase]: ...

    @classmethod
    def escape_def_name(cls, def_name: str, class_name: str) -> str: ...


class DefinitionDetector(object):
    @classmethod
    def is_device(cls, vals: List[str]) -> bool: ...

    @classmethod
    def is_vkopenurl(cls, val: str) -> bool: ...

    @classmethod
    def is_uielementrole(cls, val: str) -> bool: ...

    @classmethod
    def is_app(cls, val: str) -> bool: ...

    @classmethod
    def is_all_app(cls, vals: List[str]) -> bool: ...

    @classmethod
    def get_definition_caregory(cls, def_class: DefinitionBase) -> str: ...
