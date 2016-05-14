from typing import Iterable as Iter
from .definition import DefinitionBase


def query_filter_class_names(value: str, scope: str) -> Iter[str]: ...


class BaseTypeQuery(object):
    @classmethod
    def query(cls, value: str) -> str: ...

    def is_in(self, type: str, value: str) -> bool: ...


class DefinitionTypeQuery(BaseTypeQuery):
    def get_data(self, type: str, filepath: str) -> Iter[str]: ...


class DefinitionBucket(object):
    @classmethod
    def get_instance(cls, reset: bool = False): ...

    @classmethod
    def get_all_definitions(cls) -> Iter[DefinitionBase]: ...

    @classmethod
    def put(cls, category: str, name: str, definitions: Iter[DefinitionBase]): ...

    @classmethod
    def get(cls, category: str, name: str) -> Iter[DefinitionBase]: ...

    @classmethod
    def has(cls, category: str, name: str) -> bool: ...
