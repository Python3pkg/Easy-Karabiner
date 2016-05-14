from typing import TypeVar, Dict, Tuple, List
from .parse import Block
from .definition import DefinitionBase

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


def parse(maps: RawMaps, definitions: RawDefinitions) -> Tuple[List[Block], List[DefinitionBase]]: ...
def ensure_definitions_utf8(definitions: RawDefinitions) -> RawDefinitions: ...
def ensure_maps_utf8(maps: RawMaps) -> RawMaps: ...
def organize_maps(maps: RawMaps) -> Dict[RawFilters, List[RawKeymap]]: ...
def separate_keymap_filters(raw_map: RawMap) -> Dict[RawKeymap, RawFilters]: ...
def create_blocks(filters_keymaps_table: Dict[RawFilters, List[RawKeymap]]) -> List[Block]: ...
