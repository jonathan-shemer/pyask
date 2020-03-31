from dataclasses import Field, fields
from typing import get_args, get_origin, Tuple, Union

__all__ = ["optional_fields"]


def optional_fields(dataclass) -> Tuple[Field, ...]:
    """
    Lists all `Optional` fields in a dataclass instance or class
    :param dataclass: dataclass instance or class
    :return: tuple of all `Optional` fields of the given dataclass
    """
    dataclass_fields = fields(dataclass)
    if any(field for field in dataclass_fields if isinstance(field.type, str)):
        raise RuntimeError("Cannot interpret field types when __future__.annotations is in use")

    return tuple(field for field in dataclass_fields
                 if get_origin(field.type) is Union and type(None) in get_args(field.type))
